#include "engine/hardware_device_impl.h"

#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstring>
#include <memory>
#include <queue>
#include <tuple>

#include "akida/dense.h"
#include "akida/hw_version.h"
#include "akida/np.h"
#include "akida/shape.h"
#include "engine/dma.h"
#include "engine/dma_config_ops.h"
#include "engine/dma_desc_ops.h"
#include "engine/dma_engine.h"
#include "engine/external_mem_mgr.h"
#include "infra/int_ops.h"
#include "infra/registers_common.h"
#include "infra/system.h"

#include "dma_desc_format.h"
#include "dma_engine_ops.h"
#include "dma_events_ops.h"
#include "dma_image_ops.h"
#include "epg_ops.h"
#include "mesh.h"
#include "program_play.h"
#include "registers_dma_engine.h"
#include "registers_top_level.h"
#include "reset_nps.h"

namespace akida {

static void toggle_multi_pass(HardwareDeviceImpl* device,
                              bool enable_multi_pass);

// Get hardware version from driver
static HwVersion get_version(const HardwareDriver& driver) {
  HwVersion version{0, 0, 0, 0};
  // Try first to read IP revision from device
  const auto top_level_reg_offset = driver.top_level_reg();
  auto reg = driver.read32(top_level_reg_offset + REG_IP_VERSION);
  auto vendor_id = static_cast<uint8_t>(get_field(reg, VENDOR_ID));
  if (reg != 0) {
    auto minor_rev = static_cast<uint8_t>(get_field(reg, MINOR_REV));
    auto major_rev = static_cast<uint8_t>(get_field(reg, MAJOR_REV));
    auto prod_id = static_cast<uint8_t>(get_field(reg, PROD_ID));
    version = {vendor_id, prod_id, major_rev, minor_rev};
  } else {
    // Legacy device: rely instead on the information provided by the driver
    auto driver_desc = driver.desc();
    if (strstr(driver_desc, "NSoC_v2") != nullptr) {
      version = NSoC_v2;

    } else if (strstr(driver_desc, "NSoC_v1") != nullptr) {
      version = NSoC_v1;
    }
  }
  return version;
}

HardwareDeviceImpl::HardwareDeviceImpl(HardwareDriver* driver)
    : driver_(driver),
      version_(get_version(*driver_)),
      mesh_(nullptr),
      dma_config_{dma::Engine(dma_config_reg_base(driver_->top_level_reg()),
                              dma::config::DESC_LEN)},
      dma_event_{dma::Engine(dma_event_reg_base(driver_->top_level_reg()),
                             dma::event::DESC_LEN)},
      dma_hrc_{dma::Engine(dma_hrc_reg_base(driver_->top_level_reg()),
                           dma::hrc::DESC_LEN)},
      mem_mgr_(driver->scratch_memory(), driver->scratch_size()),
      current_program_(nullptr, 0),
      current_program_learn_en_(false),
      external_mem_(&mem_mgr_, driver) {
  if (version_ == akida::NSoC_v1) {
    panic(
        "NSoC_v1 is not supported on this version. Please install akida 2.0.5 "
        "instead.");
  }
  init();
}

HardwareDeviceImpl::~HardwareDeviceImpl() {
  dma::release(this, &dma_config_.engine);
  dma::release(this, &dma_event_.engine);
  dma::release(this, &dma_hrc_.engine);
}

HwVersion HardwareDeviceImpl::version() const { return version_; }

void HardwareDeviceImpl::dma_config_write(const dma::w32* buffer,
                                          size_t buf_size) {
  // allocate buffer length
  auto input_addr = external_mem_.reserve(buffer, buf_size * sizeof(dma::w32));
  constexpr uint32_t output_addr = 0;  // not used for write
  // format descriptor
  auto descriptor =
      dma::format_config_desc(dma::DESC_CONFIG_DIRECTION_WRITE, input_addr,
                              output_addr, static_cast<uint32_t>(buf_size));
  assert(descriptor.size() == dma::config::DESC_LEN);

  // write buffer in DDR
  external_mem_.commit(buffer, buf_size * sizeof(dma::w32));

  // tell DMA engine to process descriptor
  dma::process(driver_, dma_config_, descriptor);
  // now that input has been processed, it can be freed
  external_mem_.release(buffer);
}

void HardwareDeviceImpl::dma_config_read(dma::w32* buffer,
                                         const struct np::Ident& np,
                                         dma::Target target,
                                         uint16_t addr_target_word,
                                         uint32_t nb_words) {
  if (dma::config_block_size_needs_xl(static_cast<uint32_t>(nb_words))) {
    panic("Unsupported buffer size in config read");
  }

  // format header
  auto header =
      dma::format_config_header(np, target, nb_words, addr_target_word);
  uint32_t header_size = static_cast<uint32_t>(header.size());

  // Allocate input and output area
  auto input_addr =
      mem_mgr_.alloc(header_size * sizeof(dma::w32), MemoryMgr::Type::PROGRAM);
  // Allocation should include header size
  auto output_addr =
      mem_mgr_.alloc(nb_words * sizeof(dma::w32) + dma::kConfigReadPacketOffset,
                     MemoryMgr::Type::PROGRAM);
  // format descriptor
  auto descriptor = dma::format_config_desc(
      dma::DESC_CONFIG_DIRECTION_READ, input_addr, output_addr, header_size);
  assert(descriptor.size() == dma::config::DESC_LEN);

  // write header in DDR
  driver_->write(input_addr, header.data(), header.size() * sizeof(dma::w32));

  // tell DMA engine to process descriptor
  dma::process(driver_, dma_config_, descriptor);

  // fetch read header in DDR
  dma::wbuffer read_hdr(dma::kConfigReadPacketHdrSz);
  driver_->read(output_addr, read_hdr.data(),
                dma::kConfigReadPacketHdrSz * sizeof(dma::w32));

  // set packet size (nb of 32b words) and address/offset data
  uint32_t packetsize = dma::parse_config_read_size(read_hdr);
  uint32_t read_offset_addr = output_addr + dma::kConfigReadPacketOffset;

  if (nb_words == 0 || packetsize != nb_words) {
    panic("error on dma config read: invalid packet size (%d), expected %d.",
          packetsize, nb_words);
  }

  driver_->read(read_offset_addr, buffer, nb_words * sizeof(dma::w32));
  // now that input and outputs have been processed, it can be freed
  mem_mgr_.free(output_addr);
  mem_mgr_.free(input_addr);
}

void HardwareDeviceImpl::dma_start_config_multipass(dma::addr conf_base_address,
                                                    uint32_t num_descs,
                                                    uint32_t num_passes,
                                                    uint32_t num_extra_descs) {
  dma::start_config_multi_pass(driver_, dma_config_, conf_base_address,
                               num_descs, num_passes, num_extra_descs);
}

std::vector<TensorUniquePtr> HardwareDeviceImpl::convert_and_forward_dense(
    const std::vector<TensorConstPtr>& inputs,
    const std::vector<int32_t>* input_labels) {
  std::vector<const Tensor::Buffer*> inputs_buffers;
  inputs_buffers.reserve(inputs.size());

  // a conversion maybe needed, so we need to store the converted inputs
  std::vector<DenseConstPtr> dense_inputs;
  dense_inputs.reserve(inputs.size());
  for (const auto& input : inputs) {
    // we need to make sure the input is in akida::Dense format
    dense_inputs.push_back(Tensor::ensure_dense(input));
    auto dense = dense_inputs.back().get();
    inputs_buffers.push_back(dense->buffer());
  }
  return dma_forward(inputs_buffers, inputs.front()->dimensions(),
                     input_labels);
}

std::vector<TensorUniquePtr> HardwareDeviceImpl::convert_and_forward_sparse(
    const std::vector<TensorConstPtr>& inputs,
    const std::vector<int32_t>* input_labels) {
  std::vector<const Tensor::Buffer*> inputs_buffers;
  inputs_buffers.reserve(inputs.size());
  auto input_is_fnp = program::input_is_fnp(current_program_.first);

  // a conversion maybe needed, so we need to store the converted inputs
  std::vector<DmaEventsPtr> converted_events;
  for (const auto& input : inputs) {
    // check if we need to convert events
    const DmaEvents* events = dma_events(*input);
    // we may need to convert events to dma events
    if (events == nullptr) {
      converted_events.push_back(to_dma_events(input, input_is_fnp));
      events = converted_events.back().get();
    }
    inputs_buffers.push_back(events->buffer());
  }
  return dma_forward(inputs_buffers, inputs.front()->dimensions(),
                     input_labels);
}

std::vector<TensorUniquePtr> HardwareDeviceImpl::fit(
    const std::vector<TensorConstPtr>& inputs,
    const std::vector<int32_t>& input_labels) {
  // Check the device had been programmed
  if (!current_program_.first) {
    panic("Cannot fit without a program");
  }
  if (!current_program_learn_en_)
    panic("Learn must be enabled to call the fit method.");

  if (program::input_is_dense(current_program_.first)) {
    return convert_and_forward_dense(inputs, &input_labels);
  } else {
    return convert_and_forward_sparse(inputs, &input_labels);
  }
}

std::vector<TensorUniquePtr> HardwareDeviceImpl::forward(
    const std::vector<TensorConstPtr>& inputs) {
  // Check the device had been programmed
  if (!current_program_.first) {
    panic("Cannot forward without a program");
  }
  if (current_program_learn_en_)
    panic("Learn must be disabled to call the forward method.");

  if (program::input_is_dense(current_program_.first)) {
    return convert_and_forward_dense(inputs, nullptr);
  } else {
    return convert_and_forward_sparse(inputs, nullptr);
  }
}

const dma::Inputs& HardwareDeviceImpl::select_dma_engine(bool dense_inputs) {
  // Only enable the input DMA used by the current network:
  // HRC DMA if 1st layer is InputConvolutional, Event DMA otherwise
  dma::toggle_engine(driver_, dma_hrc_.engine.reg_base_addr, dense_inputs);
  dma::toggle_engine(driver_, dma_event_.engine.reg_base_addr, !dense_inputs);

  return dense_inputs ? dma_hrc_ : dma_event_;
}

void HardwareDeviceImpl::reset_dma_engines() {
  // Config dma descriptors are processed one at a time, but 2 descriptors will
  // need to be reserved because dma field DMA_MAX_DESC_CONTS needs to
  // be set to at least 1.
  dma::reset(this, &dma_config_.engine, dma::MIN_NB_DESCRIPTORS);
  // Event and HRC might need up to dma::MAX_NB_DESCRIPTORS descriptors
  dma::reset(this, &dma_event_.engine, dma::MAX_NB_DESCRIPTORS);
  dma::reset(this, &dma_hrc_.engine, dma::MAX_NB_DESCRIPTORS);
}

void HardwareDeviceImpl::pipeline(bool enabled) {
  dma::toggle_pipeline(driver_, dma_event_, enabled);
  dma::toggle_pipeline(driver_, dma_hrc_, enabled);
}

void HardwareDeviceImpl::toggle_clock_counter(bool enable) {
  dma::toggle_buffer_timer(driver_, dma_event_, enable);
  dma::toggle_buffer_timer(driver_, dma_hrc_, enable);
}

uint32_t HardwareDeviceImpl::read_clock_counter() {
  // read clock from HRC DMA or read from events DMA
  auto hrc_count_number = dma::read_buffer_timer(driver_, dma_hrc_);
  auto event_count_number = dma::read_buffer_timer(driver_, dma_event_);
  return std::max(hrc_count_number, event_count_number);
}

bool HardwareDeviceImpl::clock_counter_enabled() {
  return dma::is_buffer_timer_enabled(*driver_, dma_event_);
}

static void check_input_dims(const Index* program_in_dims,
                             const Shape& inputs_shape) {
  bool valid_dims = true;
  switch (inputs_shape.size()) {
    case 1:  // fully connected, 1 dimension
      if (inputs_shape[0] !=
          program_in_dims[0] * program_in_dims[1] * program_in_dims[2]) {
        valid_dims = false;
      }
      break;
    case 3:  // other cases (check only that data size is compatible)
      if (inputs_shape[0] * inputs_shape[1] * inputs_shape[2] !=
          program_in_dims[0] * program_in_dims[1] * program_in_dims[2]) {
        valid_dims = false;
      }
      break;
    default:
      valid_dims = false;
      break;
  }
  if (!valid_dims) {
    panic("Invalid input dimensions for this program");
  }
}

struct dma_job {
  uint32_t id;
  uint32_t output_address;
  const void* input;
};

std::vector<TensorUniquePtr> HardwareDeviceImpl::dma_forward(
    const std::vector<const Tensor::Buffer*>& inputs,
    const Shape& input_dimensions, const std::vector<int32_t>* labels) {
  std::vector<TensorUniquePtr> results;
  auto num_inputs = inputs.size();
  if (num_inputs == 0) {
    return results;
  }

  // verify program input dimensions match with inputs
  const auto in_dims = program::input_dims(current_program_.first);
  check_input_dims(in_dims, input_dimensions);
  const auto out_dims = program::output_dims(current_program_.first);
  const auto multi_pass = program::is_multi_pass(current_program_.first);

  // get the max possible input size & output size
  bool dense_inputs = program::input_is_dense(current_program_.first);
  auto output_format = program::output_format(current_program_.first);
  // fetch the dense input processing window from the program: it can be smaller
  // than input dimensions only for HRC valid convolutions
  auto dense_window_w = program::dense_window_w(current_program_.first);
  auto dense_window_h = program::dense_window_h(current_program_.first);

  // Output buffer has a header before the output frame
  auto output_size = out_dims[0] * out_dims[1] * out_dims[2];
  auto out_frame_size = output_frame_size(output_size, output_format);
  uint32_t out_buffer_size = output_buffer_size(out_frame_size);
  // Align output buffers to compute addresses increment
  uint32_t addr_out_increment = align_up(out_buffer_size, dma::kAlignment);

  // determine which dma controller should be used for inputs
  const auto& dma_inputs = select_dma_engine(dense_inputs);

  results.reserve(num_inputs);
  uint32_t nb_inputs_processed = 0;
  std::queue<dma_job> jobs;
  uint32_t frame_in_pool_index = 0;
  uint32_t nb_inputs_read = 0;
  // Last job id processed is read from the DMA. At reset is 0, but it keeps
  // incrementing itself
  uint32_t last_job_id_processed =
      dma::get_last_job_id_processed(driver_, dma_inputs);
  // Job id should fit in 16 bits, afer that it will restart at 0 (see
  // event::DESC_JOBID and hrc::DESC_JOBID), so it is cast to uint16_t.
  // Job id is the next one that should be processed.
  uint16_t job_id = static_cast<uint16_t>(last_job_id_processed + 1);

  // limit the number of maximum jobs: to dma::MAX_PIPELINE_SIZE for all cases
  // except in multi-pass. This will ensure that partial reconfig descriptors
  // and inputs are treated one by one, thus limiting the amount of memory usage
  // to minimum.
  auto max_jobs_size = multi_pass ? 1 : dma::MAX_PIPELINE_SIZE;

  // in multipass, an extra descriptor is used, allocate it
  dma::addr multi_pass_hw_desc = 0;
  dma::addr multi_pass_hw_payload = 0;
  if (multi_pass) {
    multi_pass_hw_desc =
        mem_mgr_.alloc(dma_inputs.engine.descriptor_len * sizeof(uint32_t),
                       MemoryMgr::Type::PROGRAM);
    multi_pass_hw_payload =
        mem_mgr_.alloc(sizeof(uint32_t), MemoryMgr::Type::PROGRAM);
  }

  // calculate number of inputs (and outputs) that will need to be present in
  // memory at the same time
  auto num_frames_pool =
      std::min(static_cast<uint32_t>(inputs.size()), max_jobs_size);
  // allocate outputs pool
  auto address_out_base =
      mem_mgr_.alloc(num_frames_pool * addr_out_increment, MemoryMgr::Type::IO);

  // loop over inputs to process them
  while (nb_inputs_read < inputs.size()) {
    // fill pipeline
    std::vector<dma::Descriptor> descriptors;
    while (nb_inputs_processed < inputs.size() && jobs.size() < max_jobs_size) {
      const auto& buffer = inputs[nb_inputs_processed];
      // get the input & output addresses
      auto address_in = external_mem_.reserve(buffer->data(), buffer->size(),
                                              MemoryMgr::Type::IO);
      auto address_out =
          address_out_base + (frame_in_pool_index * addr_out_increment);
      uint32_t learn_class = 0;
      if (labels && !labels->empty()) {
        if (labels->size() == 1)
          learn_class = labels->at(0);
        else
          learn_class = labels->at(nb_inputs_processed);
        // Labels are between 0 and N-1, but the hardware expects them between 1
        // and N, 0 meaning "any label".
        learn_class++;
      }
      // write input & generate descriptor depending on the input type
      external_mem_.commit(buffer->data(), buffer->size());
      if (dense_inputs) {
        descriptors.push_back(
            dma_dense_descriptor(address_in, address_out, job_id, learn_class,
                                 in_dims, dense_window_w, dense_window_h));
      } else {
        // buffer size must be a multiple of dma::w32
        assert(buffer->size() % sizeof(dma::w32) == 0);
        descriptors.push_back(dma::format_event_desc(
            job_id, address_in, address_out,
            static_cast<uint32_t>(buffer->size() / sizeof(dma::w32)),
            learn_class));
      }
#ifndef NDEBUG  // Debug mode enabled
      // Set the first output word (dma header) to zero.
      // This will make sure we don't parse garbage if the inference aborts
      // without any actual output being written. Note that this is only done in
      // debug to avoid performance degradation.
      driver_->write32(address_out, 0);
#endif

      jobs.push(dma_job{job_id, address_out, buffer->data()});
      nb_inputs_processed += 1;
      // increment frame_in_pool_index (circular counter)
      frame_in_pool_index = (frame_in_pool_index + 1) % max_jobs_size;
      ++job_id;
    }

    if (version() != akida::NSoC_v2) {
      // Up to NSoC_v2, the DMA input engine runtime configuration was static,
      // but the partial reconfiguration requires the DMA input engine to be
      // configured before each invocation.
      auto cur_address_out = jobs.front().output_address;
      auto num_loops = program::num_passes(current_program_.first);
      if (num_loops > 1) {
        dma::prepare_engine_multi_pass(
            driver_, dma_inputs, cur_address_out, multi_pass_hw_desc,
            multi_pass_hw_payload, num_loops, nb_inputs_processed == 0);
      }
      // When using dense/sparse outputs, we need to enable/disable the output
      // buffer automatic clearing before sending the first frame.
      // This has to be done after the multipass runtime configuration
      // because it resets the input engine.
      bool dense_outputs = program::output_is_dense(current_program_.first);
      auto clear_size = dense_outputs ? out_frame_size : 0;
      set_output_buffer_clear(driver_, dma_inputs, clear_size);
    }

    // fetch descriptors to DMA
    if (!descriptors.empty()) {
      dma::fetch_descriptors(driver_, dma_inputs.engine, descriptors);
    }
    // Wait for a new job id to be processed
    if (!multi_pass) {
      last_job_id_processed =
          dma::wait_for_new_job_id(driver_, dma_inputs, last_job_id_processed);
    } else {
      dma::wait_for_interrupt_multipass(driver_, dma_inputs);
      last_job_id_processed = jobs.front().id;
    }

    // then pop elements from the job FIFO & read outputs until we find the last
    // processed job
    uint32_t nb_inputs_fetched = 0;
    dma_job job;
    do {
      if (jobs.empty()) {
        panic("Fatal error: Job ID %d not found in Jobs ID FIFO.",
              last_job_id_processed);
      }
      job = jobs.front();
      jobs.pop();
      // free the corresponding input
      external_mem_.release(job.input);
      results.push_back(dma_events_read_outputs(driver_, job.output_address,
                                                out_dims, output_format));
      nb_inputs_fetched += 1;
    } while (job.id != last_job_id_processed);
    // Update the number of read inputs
    nb_inputs_read += nb_inputs_fetched;
  }

  // free inputs and outputs memory
  mem_mgr_.free(address_out_base);
  // free multipass extra memory
  if (multi_pass_hw_desc) {
    mem_mgr_.free(multi_pass_hw_payload);
    mem_mgr_.free(multi_pass_hw_desc);
  }

  return results;
}

// reset whole akida core, including DMAs
static void core_reset(HardwareDriver* driver) {
  const auto top_level_reg_offset = driver->top_level_reg();
  auto reg_gen_ctrl =
      driver->read32(top_level_reg_offset + REG_GENERAL_CONTROL);
  // Reset NP & CORE
  set_field(&reg_gen_ctrl, AK_CORE_RST, 1);
  set_field(&reg_gen_ctrl, SCC_CORE_RESET, 1);
  driver->write32(top_level_reg_offset + REG_GENERAL_CONTROL, reg_gen_ctrl);
  // 20 cycles should be waited. Waiting 1ms is more than enough.
  msleep(1);
  // Fields need to be reset to 0
  set_field(&reg_gen_ctrl, AK_CORE_RST, 0);
  set_field(&reg_gen_ctrl, SCC_CORE_RESET, 0);
  driver->write32(top_level_reg_offset + REG_GENERAL_CONTROL, reg_gen_ctrl);
  // 40 cycles should be waited. Waiting 1ms is more than enough.
  msleep(1);
}

void HardwareDeviceImpl::init() {
  // this core reset is only available on production chip
  core_reset(driver_);

  // reset dmas
  reset_dma_engines();

  // reset epg
  epg::epg_reset(driver_);

  // init mesh
  if (mesh_ == nullptr) {
    mesh_ = mesh::discover(this);
  }

  // reset HW mesh
  reset_nps_logic_and_cfg(driver_);

  // Pipeline is on by default
  pipeline(true);
}

const np::Mesh& HardwareDeviceImpl::mesh() const { return *mesh_; }

static void toggle_multi_pass(HardwareDeviceImpl* device,
                              bool enable_multi_pass) {
  auto driver = device->driver();
  const auto top_level_reg_offset = driver->top_level_reg();
  auto reg_gen_ctrl =
      driver->read32(top_level_reg_offset + REG_GENERAL_CONTROL);
  // toggle partial reconfig bit at top level register
  set_field(&reg_gen_ctrl, PR_MESH_RST_END, enable_multi_pass ? 1 : 0);
  driver->write32(top_level_reg_offset + REG_GENERAL_CONTROL, reg_gen_ctrl);
}

void HardwareDeviceImpl::unprogram(const uint8_t* program) {
  // Device will only unprogram provided program if provided one is the
  // programmed one.
  if (current_program_.first != program) {
    return;
  }
  // check if trying to unprogram a valid mapping
  if (program) {
    // rewind the whole program
    program::rewind(this, program);
    // disable partial reconfig and reset DMAs to go back to default
    if (program::is_multi_pass(program)) {
      toggle_multi_pass(this, false);
      // free multi pass memory
      multi_pass_memory_.free_memory(&mem_mgr_);
      // Core reset is necessary to avoid certains timeouts observed when
      // switching to single pass. These are probably due to an internal sync
      // issue between DMAs, but the core reset seems to be enough to fix the
      // problem.
      core_reset(driver_);
      reset_dma_engines();
    }
  }
  bool cc_enabled = clock_counter_enabled();
  // Reset the hardware device Mesh
  reset_nps_logic_and_cfg(driver_);
  // If clock counter was enabled, reset it
  if (cc_enabled) {
    toggle_clock_counter(false);
    toggle_clock_counter(true);
  }

  current_program_ = {nullptr, 0};
  current_program_learn_en_ = false;

  // reset I/O memory in case of leftovers due to previous exception
  mem_mgr_.reset(MemoryMgr::Type::IO);
  // reset program memory in case of leftovers due to previous exception
  external_mem_.reset();
  // Reset program memory in case of leftovers due to previous exception
  mem_mgr_.reset(MemoryMgr::Type::PROGRAM);
}

void HardwareDeviceImpl::program(const uint8_t* program, size_t size,
                                 bool learn_en) {
  if (!program) {
    panic("program should not be null");
  }
  bool reprogram = (current_program_.first != program);

  const auto can_learn = program::can_learn(program);
  if (learn_en && !can_learn) {
    panic("program cannot learn");
  }
  if (reprogram) {
    // verify program validity
    program::verify(*this, program, size);
    // Unprogram the previous mapping
    unprogram(current_program_.first);
    // Set multi pass mode
    bool multi_pass_en = program::is_multi_pass(program);
    toggle_multi_pass(this, multi_pass_en);
    if (multi_pass_en) {
      // alloc required multi pass memory
      multi_pass_memory_.alloc_memory(&mem_mgr_, program);
      program::play_multi_pass(this, program, &multi_pass_memory_);
    } else {
      program::play_single_pass(this, program);
    }
  }
  if (can_learn) {
    // Learning mode is set independently as it can be modified without
    // reprogramming
    if (program::is_multi_pass(program)) {
      program::configure_learning_mode_multi_pass(this, program,
                                                  multi_pass_memory_, learn_en);
    } else {
      program::configure_learning_mode_single_pass(this, program, learn_en);
    }
  }
  // Pipeline can only be enabled in single pass if learn is disabled
  this->pipeline(!program::is_multi_pass(program) && !learn_en);
  current_program_ = {program, size};
  current_program_learn_en_ = learn_en;
}

std::vector<TensorUniquePtr> HardwareDeviceImpl::predict(
    const std::vector<TensorConstPtr>& inputs) {
  // Check the device had been programmed
  if (!current_program_.first) {
    panic("Cannot predict without a program");
  }
  if (program::activation(current_program_.first)) {
    panic("Evaluate requires activations to be disabled");
  }
  if (current_program_learn_en_) {
    panic("Learn must be disabled to call the predict method.");
  }

  // first process all outputs
  auto outputs = program::input_is_dense(current_program_.first)
                     ? convert_and_forward_dense(inputs, nullptr)
                     : convert_and_forward_sparse(inputs, nullptr);

  const auto coords = outputs[0]->dimensions();
  assert(coords.size() == 3);
  // Prepare results vector
  std::vector<TensorUniquePtr> result;
  result.reserve(outputs.size());
  // Get potentials strides and data from program
  auto shifts = program::shifts(current_program_.first);
  auto scales = program::scales(current_program_.first);
  assert(shifts.second == scales.second);
  const auto& shift = shifts.first;
  const auto& scale = scales.first;

  for (Index i = 0; i < outputs.size(); i++) {
    // Outputs should be dense
    // move is required to convert tensor to shared_ptr, and converting a
    // unique_ptr to a shared_ptr requires an rvalue
    auto potentials = Tensor::as_dense(std::move(outputs[i]));
    assert(potentials);
    assert(potentials->layout() == Dense::Layout::RowMajor);
    // Get potentials strides and data to access them via linear index
    const auto pot_strides = potentials->strides();
    const auto pot_data = potentials->data<int32_t>();
    // Allocate a dense output in the form of a RowMajor Tensor
    auto rescaled_outputs =
        Dense::create(TensorType::float32, coords, Dense::Layout::RowMajor);
    // Get rescaled outputs data
    const auto resc_data = rescaled_outputs->data<float>();
    for (Index x = 0; x < coords[0]; x++) {
      for (Index y = 0; y < coords[1]; y++) {
        // move pointer at the beginning of the neuron
        Index coord_n0[] = {x, y, 0};
        auto coord_lin_index_n0 = linear_index(coord_n0, pot_strides);
        auto poti = &pot_data[coord_lin_index_n0];
        auto resci = &resc_data[coord_lin_index_n0];
        for (Index n = 0; n < coords[2]; n++) {
          // Evaluate rescaled output
          auto value = static_cast<float>(poti[n] - shift[n]) / scale[n];
          // Set rescaled value at the same index than output
          resci[n] = value;
        }
      }
    }
    // move is required because result contains shared_ptr, and converting a
    // unique_ptr to a shared_ptr requires an rvalue
    result.push_back(std::move(rescaled_outputs));
  }

  return result;
}

size_t HardwareDeviceImpl::learn_mem_size() const {
  return program::learn_mem_size(current_program_.first);
}

void HardwareDeviceImpl::learn_mem(uint32_t* output_buffer) {
  if (!current_program_learn_en_) {
    panic("learn is not enabled");
  }
  program::learn_mem(this, current_program_.first, output_buffer);
}

void HardwareDeviceImpl::update_learn_mem(const uint32_t* input_buffer) {
  program::update_learn_mem(this, current_program_.first, input_buffer);
}

}  // namespace akida
