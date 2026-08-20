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

    def has_maximum_length(
        self,
        response: str,
        maximum_length: int,
    ) -> bool:
        """Verifica se a resposta não ultrapassa o tamanho máximo."""
        if not self.is_not_empty(response):
            return False

        return len(response.strip()) <= maximum_length

    def is_free_of_forbidden_patterns(
        self,
        response: str,
        forbidden_patterns: list[str],
    ) -> bool:
        """Verifica se a resposta não contém padrões proibidos."""
        if not self.is_not_empty(response):
            return False

        normalized_response = response.casefold()

        return all(
            pattern.casefold() not in normalized_response
            for pattern in forbidden_patterns
        )

    def evaluate(
        self,
        response: str,
        minimum_length: int = 10,
        maximum_length: int = 1000,
        forbidden_patterns: list[str] | None = None,
    ) -> dict[str, bool]:
        """Executa todas as avaliações e retorna o resultado consolidado."""
        patterns = forbidden_patterns or []

        results = {
            "is_not_empty": self.is_not_empty(response),
            "has_minimum_length": self.has_minimum_length(
                response,
                minimum_length,
            ),
            "has_maximum_length": self.has_maximum_length(
                response,
                maximum_length,
            ),
            "is_free_of_forbidden_patterns": (
                self.is_free_of_forbidden_patterns(
                    response,
                    patterns,
                )
            ),
        }

        return {
            **results,
            "is_valid": all(results.values()),
        }