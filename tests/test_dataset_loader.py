from pathlib import Path

from src.dataset_loader import load_dataset


DATASET_PATH = Path("data/support_tickets.json")
ALLOWED_CATEGORIES = {"HARDWARE", "SOFTWARE", "ACESSO", "OUTROS"}


def test_load_dataset_returns_list():
    dataset = load_dataset(DATASET_PATH)

    assert isinstance(dataset, list)


def test_load_dataset_returns_eight_records():
    dataset = load_dataset(DATASET_PATH)

    assert len(dataset) == 8


def test_all_records_have_required_fields():
    dataset = load_dataset(DATASET_PATH)

    for record in dataset:
        assert "input" in record
        assert "expected_category" in record


def test_all_inputs_are_not_empty():
    dataset = load_dataset(DATASET_PATH)

    for record in dataset:
        assert record["input"].strip()


def test_all_categories_are_allowed():
    dataset = load_dataset(DATASET_PATH)

    for record in dataset:
        assert record["expected_category"] in ALLOWED_CATEGORIES