import sys
sys.path.insert(0, 'CAJAL/src')

from cajal.qgw import quantized_gw_parallel
import os
from os.path import join
import psutil

bd = "./swc_test_out"  # Base directory
rd = "./CAJAL/tests/test_mem/out"

@profile
def test_qgw():
    quantized_gw_parallel(
        intracell_csv_loc=join(bd, "swc_bdad_100pts_100reps_euclidean_icdm.csv"),
        num_processes=10,
        num_clusters=25,  # Each cell will be partitioned into num_clusters many clusters
        out_csv=join(rd, "quantized_gw.csv")
    )

if __name__ == "__main__":
    test_qgw()
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB") 