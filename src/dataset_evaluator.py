def calculate_accuracy(
    expected_categories: list[str],
    predicted_categories: list[str],
) -> float:
    if not expected_categories:
        raise ValueError("Expected categories cannot be empty.")

    if len(expected_categories) != len(predicted_categories):
        raise ValueError(
            "Expected and predicted categories must have the same length."
        )

    correct_predictions = sum(
        expected == predicted
        for expected, predicted in zip(
            expected_categories,
            predicted_categories,
            strict=True,
        )
    )

    return (correct_predictions / len(expected_categories)) * 100