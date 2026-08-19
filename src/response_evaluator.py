"""Regras básicas para avaliar respostas geradas por LLMs."""


class ResponseEvaluator:
    """Avalia critérios determinísticos de qualidade de uma resposta."""

    def is_not_empty(self, response: str) -> bool:
        """Verifica se a resposta contém texto válido."""
        return bool(response and response.strip())

    def has_minimum_length(
        self,
        response: str,
        minimum_length: int = 10,
    ) -> bool:
        """Verifica se a resposta possui o tamanho mínimo esperado."""
        if not self.is_not_empty(response):
            return False

        return len(response.strip()) >= minimum_length