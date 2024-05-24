import pandas as pd

parquet_file = 'test-00000-of-00001.parquet'

df = pd.read_parquet(parquet_file)
csv_file = 'test-00000-of-00001.csv'
df.to_csv(csv_file, index=False)

# If you prefer JSON, you can use the following line instead:
# json_file = 'output_file.json'
# df.to_json(json_file, orient='records', lines=True)

print(f"Parquet file has been converted to {csv_file}")