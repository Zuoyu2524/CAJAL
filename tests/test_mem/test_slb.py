import sys
sys.path.insert(0, './src')

from cajal.qgw import slb_parallel
import os
from os.path import join
import psutil
 
# Setup logging
bd = "../swc_test_out"
rd = "./tests/test_mem/out"

@profile
def test_slb():
    slb_parallel(
        join(bd, "swc_bdad_100pts_100reps_euclidean_icdm.csv"),
        out_csv=join(rd, "slb_dists.csv"),
        num_processes=10
    )


if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss  
    
    test_slb()  
    
    memory_after = process.memory_info().rss  
    print(f"Memory used by slb_parallel: {(memory_after) / 1024 / 1024:.4f} MB")
    print(f"Memory used by function: {(memory_after - memory_before) / 1024 / 1024:.4f} MB")