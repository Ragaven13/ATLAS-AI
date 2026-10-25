# from numpy.lib import stride_tricks
# from polars._utils.deprecation import P
from polars.datatypes import group
from pathlib import Path
import polars as pl
# pyrefly: ignore[missing-import]
from src.data_ingestion.bronze_writer import write_bronze

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

# print("\n Order-status distribution:")
# print(status_distribution)


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

# print("\n Missing delivery dates by status:")
# print(missing_delivery_by_status)

# Timestamp Validation


purchase_date_range = orders_df.select(

    pl.col("order_purchase_timestamp").min()
    .alias("earliest_timestamp"),
    pl.col("order_purchase_timestamp").max()
    .alias("latest_timestamp")
)

# print("\n Purchase date range:")
# print(purchase_date_range)


timestamp_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

orders_typed_df = orders_df.with_columns(
    
    [
        pl.col(column)
        .str.strptime(
            pl.Datetime,
            format="%Y-%m-%d %H:%M:%S",
            strict=False
        ).alias(column)
        for column in timestamp_columns
    ]
)

# print("\nUpdated Schema:")
# print(orders_typed_df.schema)


for column in timestamp_columns:
    orginal_nulls = orders_df[column].null_count()
    converted_nulls = orders_typed_df[column].null_count()
    
    
    parsing_failures = orginal_nulls - converted_nulls
    
    # print(f"{column}:{parsing_failures} parsing failures")
    

# Detect invalid delivery sequences

"""
identify orders where:

order_delivered_customer_date is earlier than order_purchase_timestamp.
"""

invalid_delivery = orders_df.filter(
    pl.col("order_delivered_customer_date").is_not_null()
    & (
        pl.col("order_delivered_customer_date")
        < pl.col("order_purchase_timestamp")
    )
    
)

# print("\nOrders delivered before purchase:")
# print(invalid_delivery.height)


# Empty String Validation

string_columns = [

    column
    for column,dtype in orders_df.schema.items()
    if dtype == pl.String
]

empty_values = orders_df.select(
    [
        pl.col(column)
        .str.strip_chars()
        .eq(" ")
        .sum()
        .alias(column)
        for column in string_columns
    ]
)

# print("\n Empty String Validation:")
# print(empty_values)



# DEFINE Bronze 
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze" / "olist"

# Define paraquete destination
orders_output_path = BRONZE_DIR / "orders.parquet"

written_path = write_bronze(
    df = orders_df,
    output_path = orders_output_path

)

print("Bronze file created: ", written_path)
