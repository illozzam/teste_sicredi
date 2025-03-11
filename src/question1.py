from typing import List


class Contract:
    def __init__(self, id: int, debt: int):
        """
        Representa um contrato com um associado.

        Args:
            id: Identificador único do contrato.
            debt: Saldo devedor total do contrato.
        """
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
        """
        Retorna os IDs dos N maiores devedores não renegociados.

        Args:
            open_contracts: Lista de contratos em aberto.
            renegotiated_contracts: Lista de IDs de contratos renegociados.
            top_n: Número de devedores a serem retornados.

        Returns:
            Lista de IDs dos top N devedores não renegociados, ordenada decrescentemente pelo débito.

        Exemplo:
            >>> contracts = [Contract(1, 100), Contract(2, 200), Contract(3, 300)]
            >>> renegotiated = [3]
            >>> top_n = 2
            >>> get_top_N_open_contracts(contracts, renegotiated, top_n)
            [2, 1]
        """
        renegotiated_set = set(renegotiated_contracts)

        filtered_contracts = [
            contract
            for contract in open_contracts
            if contract.id not in renegotiated_set
        ]

        sorted_contracts = sorted(
            filtered_contracts, key=lambda contract: -contract.debt
        )

        if top_n <= 0 or not sorted_contracts:
            return []

        top_n = min(top_n, len(sorted_contracts))
        return [contract.id for contract in sorted_contracts[:top_n]]
