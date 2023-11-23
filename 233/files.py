import os
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def _get_create_date(file):
    return datetime.fromtimestamp(file.stat().st_ctime)


def _get_archive_name(file):
    created = _get_create_date(file).strftime("%Y-%m-%d")
    return f"{file.stem}_{created}{file.suffix}"


def zip_last_n_files(directory: Path = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3):
    files = sorted(
        [item for item in directory.glob("*") if item.is_file()],
        key=_get_create_date,
        reverse=True,
    )

    with ZipFile(zip_file, "w") as myzip:
        for file in files[:n]:
            myzip.write(file, arcname=_get_archive_name(file))
