"""Testes das regras de avaliação de respostas."""

from src.response_evaluator import ResponseEvaluator


def test_should_accept_non_empty_response():
    evaluator = ResponseEvaluator()

    assert evaluator.is_not_empty("Resposta válida")


def test_should_reject_empty_response():
    evaluator = ResponseEvaluator()

    assert not evaluator.is_not_empty("")


def test_should_reject_response_with_only_spaces():
    evaluator = ResponseEvaluator()

    assert not evaluator.is_not_empty("   ")


def test_should_accept_response_with_minimum_length():
    evaluator = ResponseEvaluator()

    assert evaluator.has_minimum_length("Resposta válida")


def test_should_reject_response_below_minimum_length():
    evaluator = ResponseEvaluator()

    assert not evaluator.has_minimum_length("Curta")


def test_should_reject_empty_response_in_length_validation():
    evaluator = ResponseEvaluator()

    assert not evaluator.has_minimum_length("")