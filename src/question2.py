from typing import List


class Orders:
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        """
        Calcula o número mínimo de viagens para atender todas as requisições,
        combinando no máximo 2 por viagem.

        Args:
            requests: Lista de valores monetários solicitados pelas agências.
            n_max: Valor máximo permitido por viagem.

        Returns:
            Número mínimo de viagens necessárias.

        Exemplo:
            >>> combine_orders([70, 30, 10], 100)
            2  # Combina 70+30 e 10 sozinho
        """
        if not requests:
            return 0

        sorted_requests = sorted(requests, reverse=True)
        high_ptr = 0  # Ponteiro para o maior valor restante
        low_ptr = len(sorted_requests) - 1  # Ponteiro para o menor valor restante
        trips = 0

        while high_ptr <= low_ptr:
            # Tenta combinar o maior e o menor valores restantes
            if sorted_requests[high_ptr] + sorted_requests[low_ptr] <= n_max:
                low_ptr -= 1  # Combina e move o ponteiro do menor valor
            high_ptr += 1  # Move o ponteiro do maior valor (mesmo que não combine)
            trips += 1

        return trips
