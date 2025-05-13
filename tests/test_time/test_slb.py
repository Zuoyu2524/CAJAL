import sys
sys.path.insert(0, 'CAJAL/src')

from cajal.qgw import slb_parallel
from os.path import join
import timeit

# Setup logging
bd = "./swc_test_out"
rd = "./test_time/out"

def test_slb():
    slb_parallel(
        join(bd, "swc_bdad_100pts_100reps_euclidean_icdm.csv"),
        out_csv=join(rd, "slb_dists.csv"),
        num_processes=10
    )

if __name__ == '__main__':
    times = timeit.repeat('test_slb()', globals=globals(), repeat=1, number=1)
    average_time = sum(times) / len(times)
    print(f"average running time: {average_time:.4f} s")
    print(f"total running time: {times}")