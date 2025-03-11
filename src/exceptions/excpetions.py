class InvalidContractError(Exception):
    """Exceção para erros relacionados a contratos inválidos."""

    ...


class InvalidOrderError(Exception):
    """Exceção para erros relacionados a requisições de pedidos inválidas."""

    ...


class BusinessRuleError(Exception):
    """Exceção para violações de regras de negócio (ex.: débito negativo)."""

    ...
