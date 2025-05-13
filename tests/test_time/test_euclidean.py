import sys
sys.path.insert(0, 'CAJAL/src')

import cajal.sample_swc
import cajal.swc
import os
from os.path import join
import timeit

bd = "./subsampled"  # Base directory
rd = "./CAJAL/tests/test_time/out"

def test_euclidean_dist():
    cajal.sample_swc.compute_icdm_all_euclidean(
        infolder=bd,
        out_csv=join(rd, 'swc_bdad_100pts_100reps_euclidean_icdm.csv'),
        out_node_types=join(
            rd, 'swc_bdad_100pts_100reps_euclidean_node_types.npy'),  # save node types

        # preprocessing
        preprocess=cajal.swc.preprocessor_eu(
            structure_ids='keep_all_types',  # keep all node types
            soma_component_only=False),  # keep the entire neuron
        num_processes=32,  # number of process for multi-threading
        n_sample=100  # number of sample points
    )
if __name__ == '__main__':
    times = timeit.repeat('test_euclidean_dist()', globals=globals(), repeat=100, number=1)
    average_time = sum(times) / len(times)
    print(f"average running time: {average_time:.4f} s")
    print(f"total running time: {times}")