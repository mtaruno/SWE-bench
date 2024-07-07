#!/bin/bash
python swebench/harness/run_evaluation.py \
    --predictions_path "inference/outputs/gpt-4-0125-preview__SWE-bench_Lite_oracle__test.jsonl"  \
    --swe_bench_tasks princeton-nlp/SWE-bench_Lite_oracle  \
    --log_dir "inference/evaluate/run2/log_directory" \
    --testbed "inference/evaluate/run2/testbed" \
    --skip_existing \
    --timeout 900 \
    --verbose