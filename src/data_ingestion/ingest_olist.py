from polars.datatypes import group
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

# # Print first 5 rows
# print("\n First 5 rows:")
# print(orders_df.head())


# # Inspect the DataFrame
# print("\n Dataset shape:")
# print(orders_df.shape)

# # Print column names
# print("\n Column names:")
# print(orders_df.columns)

# # Inspect data types
# print("\n Dataset schemas:")
# print(orders_df.schema)

# # count missing values
# print("\n Missing values:")
# print(orders_df.null_count())

# # count unique order ID's

# unique_orders = orders_df['order_id'].n_unique()

# # Calculate duplicate count
# duplicate_count = orders_df.height - unique_orders

# print("Total Orders:", orders_df.height)
# print("Unique Orders:", unique_orders)
# print("Duplicate Orders:", duplicate_count)


# Order-status distribution
status_distribution= (
    orders_df
    .group_by("order_status")
    .agg(
        pl.len().alias("order_count")
    )
    .sort("order_count", descending=True)
)

print("\n Order-status distribution:")
print(status_distribution)


missing_delivery_by_status = (
    orders_df
    .group_by("order_status")
    .agg(
        pl.len().alias("total_orders"),
        pl.col("order_delivered_customer_date")
        .is_null()
        .sum()
        .alias("missing_delivery_dates")
        
    )
    .sort("missing_delivery_dates", descending=True)
)

print("\n Missing delivery dates by status:")
print(missing_delivery_by_status)