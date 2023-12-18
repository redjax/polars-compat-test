import sys

sys.path.append(".")

from pathlib import Path

from core.constants import (
    DATA_DIR,
    DATASET_DIR,
    DATASET_PQ_DIR,
    DATASET_RAW_DIR,
    CC_FRAUD_PROJ_NAME,
    BEE_PROJ_NAME,
)

import polars as pl

from pl_test.utils.proj_data import get_raw_files


def main():
    bee_raw_files = get_raw_files(proj_name=BEE_PROJ_NAME)
    print(
        f"Loaded [{len(bee_raw_files)}] file(s) from {DATASET_RAW_DIR}/{BEE_PROJ_NAME}"
    )

    cc_fraud_raw_files = get_raw_files(proj_name=CC_FRAUD_PROJ_NAME)
    print(
        f"Loaded [{len(cc_fraud_raw_files)}] file(s) from {DATASET_RAW_DIR}/{CC_FRAUD_PROJ_NAME}"
    )


if __name__ == "__main__":
    main()
