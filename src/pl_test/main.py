import sys

sys.path.append(".")

from pathlib import Path

import polars as pl

DATASET_DIR: Path = Path("dataset")
DATASET_RAW_DIR: Path = Path(f"{DATASET_DIR}/raw")
DATASET_PQ_DIR: Path = Path(f"{DATASET_DIR}/pq")


def load_raw_csvs_to_dfs(scan_dir: Path = DATASET_RAW_DIR) -> list[pl.DataFrame]:
    dfs = []

    for f in DATASET_RAW_DIR.glob("*.csv"):
        try:
            _df = pl.read_csv(f)

            dfs.append(_df)

        except Exception as exc:
            raise Exception(f"Unhandled exception reading Parquet file. Details: {exc}")

    return dfs


def load_csv_to_df(csv_path: Path = None) -> pl.DataFrame:
    try:
        df = pl.read_csv(csv_path)

        return df

    except Exception as exc:
        raise Exception(
            f"Unhandled exception reading CSV file at path: {csv_path}. Details: {exc}"
        )


if __name__ == "__main__":
    print("Test Polars")
    test_csv = f"{DATASET_RAW_DIR}/BIP Bee Colony Loss Clean.csv"

    all_csv_dfs = load_raw_csvs_to_dfs()
    test_df = load_csv_to_df(csv_path=test_csv)

    print(test_df.shape)
    print(test_df.head(5))
    print(test_df.columns)
