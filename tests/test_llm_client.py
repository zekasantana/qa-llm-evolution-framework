from unittest.mock import MagicMock

import pytest

from src.llm_client import LLMClient


def test_should_generate_response_with_mocked_client():
    mocked_client = MagicMock()
    mocked_client.responses.create.return_value.output_text = " HARDWARE "

    llm_client = LLMClient(
        model="test-model",
        client=mocked_client,
    )

    result = llm_client.generate_response(" Classifique o chamado ")

    assert result == "HARDWARE"
    mocked_client.responses.create.assert_called_once_with(
        model="test-model",
        input="Classifique o chamado",
    )


@pytest.mark.parametrize("prompt", ["", "   ", "\n\t"])
def test_should_reject_empty_prompt(prompt):
    llm_client = LLMClient(client=MagicMock())

    with pytest.raises(
        ValueError,
        match="O prompt não pode ser vazio.",
    ):
        llm_client.generate_response(prompt)


def test_should_reject_missing_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(
        ValueError,
        match="OPENAI_API_KEY não configurada.",
    ):
        LLMClient()


def test_should_use_model_from_environment(monkeypatch):
    monkeypatch.setenv("OPENAI_MODEL", "model-from-environment")

    llm_client = LLMClient(client=MagicMock())

    assert llm_client.model == "model-from-environment"


def test_should_use_default_model(monkeypatch):
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    llm_client = LLMClient(client=MagicMock())

    assert llm_client.model == "gpt-5-mini"