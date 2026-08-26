import json
from pathlib import Path


def load_dataset(file_path: str | Path) -> list[dict[str, str]]:
    path = Path(file_path)

    with path.open(encoding="utf-8") as dataset_file:
        dataset = json.load(dataset_file)

    return dataset