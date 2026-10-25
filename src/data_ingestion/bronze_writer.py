from asyncio import coroutines
from pathlib import Path
import polars as pl


def write_bronze(
    df:pl.DataFrame,
    output_path: Path
) -> Path:
    """
    Write a Polars DataFrame to the Bronze layer.

    Args:
        df: Source DataFrame.
        output_path: Destination Parquet file.

    Returns:
        Path to the written Parquet file.
    """


    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.write_parquet(output_path, compression='zstd')


    if not output_path.exists():
        raise FileNotFoundError(f"Bronze output was not created: {output_path}")
    
    written_df = pl.read_parquet(output_path)
    
    if written_df.height != df.height:
        raise ValueError(
            "Bronze row count does not match source row count"
        )

        return output_path
    



    