from swebench.metrics.report import get_model_report

model = "gpt-4-0125-preview" # "Model name (same as moniker used for predictions)"
predictions_path = "inference/outputs/gpt-4-0125-preview__SWE-bench_Lite_oracle__test.jsonl" # "Path to predictions .json file"
swe_bench_tasks = "swe-bench.json" # "Path to `swe-bench.json` file"
log_dir = "" # "Path to folder with per-task instance logs (same as `log_dir` from above)"

report = get_model_report(model, predictions_path, swe_bench_tasks, log_dir)

for k, v in report.items():
    print(f"- {k}: {len(v)}")
