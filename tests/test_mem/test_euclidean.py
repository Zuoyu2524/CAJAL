import sys
sys.path.insert(0, 'CAJAL/src')

import cajal.sample_swc
import cajal.swc
import os
from os.path import join
import psutil

bd = "./subsampled"  # Base directory
rd = "./CAJAL/tests/test_mem/out"

@profile
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
    test_euclidean_dist()
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(f"Memory usage: {memory_info.rss / 1024 / 1024} MB") 