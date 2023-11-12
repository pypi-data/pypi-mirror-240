import torch
import torch.distributed as dist
from .coflog import default_logger
def report_memory_usage(msg="", rank=0):
    # MC: Memory Allocated in Current
    # MM: Memory Allocated in Max
    # MR: Memory Reserved by PyTorch
    def check_rank(rank):
        return not dist.is_initialized() or dist.get_rank()==rank
    GB = 1024*1024*1024
    if check_rank(rank):
        default_logger.info(f"{msg} GPU Memory Report (GB): MA = {torch.cuda.memory_allocated()/GB:.2f} | "
                        f"MM = {torch.cuda.max_memory_allocated()/GB:.2f} | "
                        f"MR = {torch.cuda.memory_reserved()/GB:.2f}")