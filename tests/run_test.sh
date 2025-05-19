#!/bin/bash

LOG_DIR="../logs_new_mem"
mkdir -p "$LOG_DIR"

NUM_TESTS=10
SLEEP_TIME=20  

# echo "Time evaluation"

# python ./tests/test_time/test_euclidean.py > "$LOG_DIR/time_0_run_0.log" 2>&1 &
# wait
# python ./tests/test_time/test_qgw.py > "$LOG_DIR/time_1_run_0.log" 2>&1 &
# wait
# python ./tests/test_time/test_slb.py > "$LOG_DIR/time_2_run_0.log" 2>&1 &
# wait

echo "Memory evaluation"

file_list=("test_euclidean.py" "test_qgw.py" "test_slb.py")

for index in "${!file_list[@]}"; do
    file="${file_list[$index]}"
    total_proc=0
    total_func=0

    for i in $(seq 1 $NUM_TESTS); do
        log_file="$LOG_DIR/mem_${index}_run_$i.log"
        python -m memory_profiler ./tests/test_mem/"$file" > "$log_file" 2>&1

        mem_proc=$(grep -oE 'Memory used by [a-zA-Z_]+: [0-9]+\.[0-9]+ MB' "$log_file" | head -n1 | awk '{print $5}')

        mem_func=$(grep -oE 'Memory used by function: [0-9]+\.[0-9]+ MB' "$log_file" | awk '{print $5}')

        if [[ -n "$mem_proc" && -n "$mem_func" ]]; then
            total_proc=$(echo "$total_proc + $mem_proc" | bc)
            total_func=$(echo "$total_func + $mem_func" | bc)
        else
            echo "Warning: Missing memory data in $log_file"
        fi

        sleep $SLEEP_TIME
    done

    avg_proc=$(echo "scale=2; $total_proc / $NUM_TESTS" | bc)
    avg_func=$(echo "scale=2; $total_func / $NUM_TESTS" | bc)

    echo "The average process memory usage for $file is $avg_proc MB"
    echo "The average function memory increase for $file is $avg_func MB"
done

echo "All jobs completed."