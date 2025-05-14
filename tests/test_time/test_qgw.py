import sys
sys.path.insert(0, './src')

from cajal.qgw import quantized_gw_parallel
from os.path import join
import timeit

bd = "../swc_test_out"
rd = "./tests/test_time/out"

def test_qgw():
    quantized_gw_parallel(
        intracell_csv_loc=join(bd, "swc_bdad_100pts_100reps_euclidean_icdm.csv"),
        num_processes=10,
        num_clusters=25,  # Each cell will be partitioned into num_clusters many clusters
        out_csv=join(rd, "quantized_gw.csv")
    )

if __name__ == '__main__':
    times = timeit.repeat('test_qgw()', globals=globals(), repeat=100, number=1)
    average_time = sum(times) / len(times)
    print(f"average running time: {average_time:.4f} s")
    print(f"total running time: {times}")