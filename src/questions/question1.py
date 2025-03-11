from typing import List

from exceptions import BusinessRuleError, InvalidContractError


class Contract:
    def __init__(self, id: int, debt: int):
        if not isinstance(id, int) or id <= 0:
            raise InvalidContractError("ID do contrato deve ser um inteiro positivo.")
        if not isinstance(debt, int) or debt < 0:
            raise BusinessRuleError("Dívida não pode ser negativa.")

        self.id = id
        self.debt = debt

    def __str__(self) -> str:
        return f"id={self.id}, debt={self.debt}"


class Contracts:
    def get_top_N_open_contracts(
        self,
        open_contracts: List[Contract],
        renegotiated_contracts: List[int],
        top_n: int,
    ) -> List[int]:
        if not isinstance(open_contracts, list):
            raise InvalidContractError("open_contracts deve ser uma lista.")
        if not all(isinstance(c, Contract) for c in open_contracts):
            raise InvalidContractError(
                "Elementos de open_contracts devem ser do tipo Contract."
            )
        if not isinstance(renegotiated_contracts, list):
            raise InvalidContractError(
                "renegotiated_contracts deve ser uma lista de inteiros."
            )
        if not all(isinstance(id, int) for id in renegotiated_contracts):
            raise InvalidContractError(
                "renegotiated_contracts contém elementos não inteiros."
            )
        if not isinstance(top_n, int) or top_n < 0:
            raise InvalidContractError("top_n deve ser um inteiro não negativo.")

        renegotiated_set = set(renegotiated_contracts)
        filtered_contracts = [c for c in open_contracts if c.id not in renegotiated_set]

        if not filtered_contracts:
            return []

        sorted_contracts = sorted(filtered_contracts, key=lambda x: -x.debt)
        top_n = min(top_n, len(sorted_contracts))

        return [c.id for c in sorted_contracts[:top_n]]
