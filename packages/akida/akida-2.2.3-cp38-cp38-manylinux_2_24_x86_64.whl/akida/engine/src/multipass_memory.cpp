#include "engine/multipass_memory.h"
#include "engine/memory_mgr.h"

#include "program_play.h"

namespace akida {

void MultiPassMemory::alloc_memory(MemoryMgr* memory_mgr,
                                   const uint8_t* program) {
  dummy_output_addr =
      memory_mgr->alloc(sizeof(dma::w32), MemoryMgr::Type::PROGRAM);
  descriptors_addr = memory_mgr->alloc(
      program::multi_pass_descriptors_required_memory(program),
      MemoryMgr::Type::PROGRAM);
}

void MultiPassMemory::free_memory(MemoryMgr* memory_mgr) {
  // we need to free descriptors area
  memory_mgr->free(descriptors_addr);
  // we need to free dummy output
  memory_mgr->free(dummy_output_addr);
}

void MultiPassMemory::update_learn_descriptor_addr(
    dma::addr learn_descriptor_address) {
  learn_descriptor_addr = learn_descriptor_address;
}

}  // namespace akida
