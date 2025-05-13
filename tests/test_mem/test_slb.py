from cajal.qgw import slb_parallel
import os
from os.path import join
import psutil
 
# Setup logging
bd = "./swc_test_out"
rd = "./CAJAL/tests/test_mem/out"
@profile
def test_slb():
    slb_parallel(
        join(bd, "swc_bdad_100pts_100reps_euclidean_icdm.csv"),
        out_csv=join(rd, "slb_dists.csv"),
        num_processes=10
    )


if __name__ == "__main__":
    test_slb()
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB") 