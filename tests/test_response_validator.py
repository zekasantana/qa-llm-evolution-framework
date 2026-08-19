import pytest

from src.response_validator import is_valid_category, normalize_category


def test_should_normalize_category() -> None:
    response = "  hardware  "

    result = normalize_category(response)

    assert result == "HARDWARE"


@pytest.mark.parametrize(
    "category",
    [
        "HARDWARE",
        "SOFTWARE",
        "ACESSO",
        "OUTROS",
    ],
)
def test_should_accept_allowed_categories(category: str) -> None:
    assert is_valid_category(category)


def test_should_reject_response_with_explanation() -> None:
    response = "HARDWARE porque o monitor não está funcionando"

    assert not is_valid_category(response)


def test_should_reject_empty_response() -> None:
    assert not is_valid_category("")