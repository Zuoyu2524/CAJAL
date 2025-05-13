#!/bin/bash

LOG_DIR="./logs_new"
mkdir -p "$LOG_DIR"

echo "time evaluation"

# python3 ./CAJAL/tests/test_time/test_euclidean.py > "$LOG_DIR/run_1.log" 2>&1 &
# python3 ./CAJAL/tests/test_time/test_qgw.py > "$LOG_DIR/run_2.log" 2>&1 &
# python3 ./CAJAL/tests/test_time/test_slb.py > "$LOG_DIR/run_3.log" 2>&1 &

echo "memory evaluation"

# mprof run --python ./CAJAL/tests/test_mem/test_euclidean.py > "$LOG_DIR/run_4.log" 2>&1 &
mprof run --python ./CAJAL/tests/test_mem/test_qgw.py > "$LOG_DIR/run_5.log" 2>&1 &
# mprof run --python ./CAJAL/tests/test_mem/test_slb.py > "$LOG_DIR/run_6.log" 2>&1 &

wait

echo "All jobs completed."