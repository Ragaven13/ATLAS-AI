
from pathlib import Path
import polars as pl


def write_bronze(df: pl.DataFrame, output_path: Path) -> Path:

    # Step 1: Create the destination directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Step 2: Write DataFrame to Parquet
    df.write_parquet(output_path, compression="zstd")

    # Step 3: Verify file existence
    if not output_path.is_file():
        raise FileNotFoundError(
            f"Bronze output was not created: {output_path}"
        )

    # Step 4: Read the Parquet file back
    written_df = pl.read_parquet(output_path)

    # Step 5: Validate row count
    if written_df.height != df.height:
        raise ValueError(
            "Bronze row count does not match source row count"
        )

    # Step 6: Validate schema
    if written_df.schema != df.schema:
        raise ValueError(
            "Bronze schema does not match source schema"
        )

    # Step 7: Validate data integrity
    if not written_df.equals(df):
        raise ValueError(
            "Bronze data does not match source data"
        )

    # Step 8: Return the output path
    return output_path
