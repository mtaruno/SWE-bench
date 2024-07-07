from report import get_model_report
from swebench.metrics.report import get_model_report

model = "gpt-4-0125-preview" # "Model name (same as moniker used for predictions)"
predictions_path = "/Users/matthewtaruno/Desktop/SWE-bench/inference/outputs/gpt-4-0125-preview__SWE-bench_Lite_oracle__test.jsonl" # "Path to predictions .json file"
swe_bench_tasks = "princeton-nlp/SWE-bench_Lite_oracle" #"/Users/matthewtaruno/Desktop/SWE-bench/SWE-bench-lite/swe-bench-lite.json" # "Path to `swe-bench.json` file"
log_dir = "/Users/matthewtaruno/Desktop/SWE-bench/inference/evaluate/run2/log_directory" # "Path to folder with per-task instance logs (same as `log_dir` from above)"

model = "glm-4" # "gpt-4-0125-preview" # "Model name (same as moniker used for predictions)"
predictions_path = "/Users/matthewtaruno/Desktop/SWE-bench/inference/outputs/glm-4__SWE-bench_Lite_oracle__test.jsonl"# "Path to predictions .json file"
swe_bench_tasks = "princeton-nlp/SWE-bench_Lite_oracle" # "Path to `swe-bench.json` file"
log_dir = "/Users/matthewtaruno/Desktop/SWE-bench/inference/evaluate/run3/log_directory/glm-4" # "Path to folder with per-task instance logs (same as `log_dir` from above)"
report = get_model_report(model, predictions_path, swe_bench_tasks, log_dir)

for k, v in report.items():
    print(f"- {k}: {len(v)}")


