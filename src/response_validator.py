ALLOWED_CATEGORIES = {
    "HARDWARE",
    "SOFTWARE",
    "ACESSO",
    "OUTROS",
}


def normalize_category(response: str) -> str:
    """Remove espaços extras e converte a resposta para letras maiúsculas."""
    return response.strip().upper()


def is_valid_category(response: str) -> bool:
    """Verifica se a resposta corresponde a uma categoria permitida."""
    normalized_response = normalize_category(response)
    return normalized_response in ALLOWED_CATEGORIES