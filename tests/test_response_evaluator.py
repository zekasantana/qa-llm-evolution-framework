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


def test_should_accept_response_without_forbidden_patterns():
    evaluator = ResponseEvaluator()
    forbidden_patterns = ["não posso ajudar", "como inteligência artificial"]

    result = evaluator.is_free_of_forbidden_patterns(
        "Para resolver o problema, reinicie o equipamento.",
        forbidden_patterns,
    )

    assert result


def test_should_reject_response_with_forbidden_pattern():
    evaluator = ResponseEvaluator()
    forbidden_patterns = ["não posso ajudar", "como inteligência artificial"]

    result = evaluator.is_free_of_forbidden_patterns(
        "Como inteligência artificial, não posso realizar essa ação.",
        forbidden_patterns,
    )

    assert not result


def test_should_ignore_case_when_checking_forbidden_patterns():
    evaluator = ResponseEvaluator()
    forbidden_patterns = ["não posso ajudar"]

    result = evaluator.is_free_of_forbidden_patterns(
        "NÃO POSSO AJUDAR com essa solicitação.",
        forbidden_patterns,
    )

    assert not result


def test_should_reject_empty_response_in_forbidden_patterns_validation():
    evaluator = ResponseEvaluator()

    assert not evaluator.is_free_of_forbidden_patterns("", ["erro"])


def test_should_accept_response_within_maximum_length():
    evaluator = ResponseEvaluator()

    result = evaluator.has_maximum_length(
        "Resposta válida",
        maximum_length=20,
    )

    assert result


def test_should_reject_response_above_maximum_length():
    evaluator = ResponseEvaluator()

    result = evaluator.has_maximum_length(
        "Esta resposta ultrapassa o limite configurado.",
        maximum_length=20,
    )

    assert not result


def test_should_reject_empty_response_in_maximum_length_validation():
    evaluator = ResponseEvaluator()

    assert not evaluator.has_maximum_length("", maximum_length=20)

def test_should_approve_response_when_all_criteria_are_valid():
    evaluator = ResponseEvaluator()

    result = evaluator.evaluate(
        response="Reinicie o equipamento e tente novamente.",
        minimum_length=10,
        maximum_length=100,
        forbidden_patterns=["não posso ajudar"],
    )

    assert result == {
        "is_not_empty": True,
        "has_minimum_length": True,
        "has_maximum_length": True,
        "is_free_of_forbidden_patterns": True,
        "is_valid": True,
    }


def test_should_reject_evaluation_with_forbidden_pattern():
    evaluator = ResponseEvaluator()

    result = evaluator.evaluate(
        response="Não posso ajudar com essa solicitação.",
        minimum_length=10,
        maximum_length=100,
        forbidden_patterns=["não posso ajudar"],
    )

    assert not result["is_free_of_forbidden_patterns"]
    assert not result["is_valid"]


def test_should_reject_evaluation_above_maximum_length():
    evaluator = ResponseEvaluator()

    result = evaluator.evaluate(
        response="Esta resposta ultrapassa o limite configurado.",
        minimum_length=10,
        maximum_length=20,
        forbidden_patterns=[],
    )

    assert not result["has_maximum_length"]
    assert not result["is_valid"]