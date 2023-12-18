from pathlib import Path

from core.constants import DATA_DIR, DATASET_DIR, DATASET_PQ_DIR, DATASET_RAW_DIR


def get_raw_files(proj_name: str = None, filetype: str = ".csv") -> list[Path]:
    proj_raw_files: list[Path] = []
    proj_raw_dir: Path = Path(f"{DATASET_RAW_DIR}/{proj_name}")

    if not proj_raw_dir.exists():
        raise FileNotFoundError(f"Could not find project raw data dir: {proj_raw_dir}")

    if filetype is None:
        search_str = "**/*"
    else:
        if not filetype.startswith("."):
            filetype: str = f".{filetype}"

        search_str = f"**/*{filetype}"

    for f in proj_raw_dir.glob(search_str):
        if f.is_file():
            proj_raw_files.append(f)

    return proj_raw_files
