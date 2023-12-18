from pathlib import Path

DATA_DIR: Path = Path(".data")

DATASET_DIR: Path = Path(f"{DATA_DIR}/datasets")
DATASET_RAW_DIR: Path = Path(f"{DATASET_DIR}/raw")
DATASET_PQ_DIR: Path = Path(f"{DATASET_DIR}/pq")

BEE_PROJ_NAME: Path = Path("bee_colony")
