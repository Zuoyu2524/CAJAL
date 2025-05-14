import sys
sys.path.insert(0, './src')

import cajal.sample_swc
import cajal.swc
import os
from os.path import join
import psutil

bd = "../subsampled"  # Base directory
rd = "./tests/test_mem/out"

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
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss 

    test_euclidean_dist()

    memory_after = process.memory_info().rss  
    print(f"Memory used by euclidean_dist: {(memory_after) / 1024 / 1024:.4f} MB")
    print(f"Memory used by function: {(memory_after - memory_before) / 1024 / 1024:.4f} MB")