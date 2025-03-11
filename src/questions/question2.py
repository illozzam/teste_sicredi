from typing import List

from exceptions import BusinessRuleError, InvalidOrderError


class Orders:
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        if not isinstance(requests, list):
            raise InvalidOrderError("requests deve ser uma lista de inteiros.")
        if not all(isinstance(r, int) and r > 0 for r in requests):
            raise BusinessRuleError("Requisições devem ser inteiros positivos.")
        if not isinstance(n_max, int) or n_max <= 0:
            raise InvalidOrderError("n_max deve ser um inteiro positivo.")
        if not requests:
            return 0

        for req in requests:
            if req > n_max:
                raise BusinessRuleError(
                    f"Requisição {req} excede o valor máximo permitido ({n_max})."
                )

        requests_sorted = sorted(requests, reverse=True)
        high_ptr = 0
        low_ptr = len(requests_sorted) - 1
        trips = 0

        while high_ptr <= low_ptr:
            if requests_sorted[high_ptr] + requests_sorted[low_ptr] <= n_max:
                low_ptr -= 1
            high_ptr += 1
            trips += 1

        return trips
