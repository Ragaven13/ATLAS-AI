from pathlib import Path
import polars as pl

PROJECT_ROOT = Path(__file__).resolve().parents[2]

print(PROJECT_ROOT)

RAW_DATA  = PROJECT_ROOT / "data" / "raw" / "olist"

# print("DIRECTORY exists:", RAW_DATA.is_dir())

csv_files = sorted(RAW_DATA.glob("*.csv"))

# for csv_file in csv_files:
#     print(csv_file.name)

# print("Total CSV files", len(csv_files))


orders_path = RAW_DATA / "olist_orders_dataset.csv"


orders_df = pl.read_csv(orders_path)

# Print first 5 rows
print("\n First 5 rows:")
print(orders_df.head())


# Inspect the DataFrame
print("\n Dataset shape:")
print(orders_df.shape)

# Print column names
print("\n Column names:")
print(orders_df.columns)

# Inspect data types
print("\n Dataset schemas:")
print(orders_df.schema)

# count missing values
print("\n Missing values:")
print(orders_df.null_count())


