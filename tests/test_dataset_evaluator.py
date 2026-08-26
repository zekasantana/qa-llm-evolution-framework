import pytest

from src.dataset_evaluator import calculate_accuracy


def test_calculate_accuracy_returns_one_hundred_for_all_correct():
    expected = ["HARDWARE", "SOFTWARE", "ACESSO", "OUTROS"]
    predicted = ["HARDWARE", "SOFTWARE", "ACESSO", "OUTROS"]

    accuracy = calculate_accuracy(expected, predicted)

    assert accuracy == 100.0


def test_calculate_accuracy_returns_fifty_for_half_correct():
    expected = ["HARDWARE", "SOFTWARE", "ACESSO", "OUTROS"]
    predicted = ["HARDWARE", "OUTROS", "ACESSO", "SOFTWARE"]

    accuracy = calculate_accuracy(expected, predicted)

    assert accuracy == 50.0


def test_calculate_accuracy_returns_zero_for_all_incorrect():
    expected = ["HARDWARE", "SOFTWARE"]
    predicted = ["SOFTWARE", "HARDWARE"]

    accuracy = calculate_accuracy(expected, predicted)

    assert accuracy == 0.0


def test_calculate_accuracy_rejects_empty_expected_categories():
    with pytest.raises(
        ValueError,
        match="Expected categories cannot be empty.",
    ):
        calculate_accuracy([], [])


def test_calculate_accuracy_rejects_different_list_lengths():
    expected = ["HARDWARE", "SOFTWARE"]
    predicted = ["HARDWARE"]

    with pytest.raises(
        ValueError,
        match="Expected and predicted categories must have the same length.",
    ):
        calculate_accuracy(expected, predicted)