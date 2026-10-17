from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

print(PROJECT_ROOT)

RAW_DATA  = PROJECT_ROOT / "data" / "raw" / "olist"

print("DIRECTORY exists:", RAW_DATA.is_dir())

csv_files = sorted(RAW_DATA.glob("*.csv"))

for csv_file in csv_files:
    print(csv_file.name)

print("Total CSV files", len(csv_files))

