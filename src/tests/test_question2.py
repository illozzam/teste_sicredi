import unittest

from exceptions import BusinessRuleError, InvalidOrderError
from questions import Orders


class TestOrders(unittest.TestCase):
    def test_combine_orders(self):
        orders = Orders()

        # Exemplo do problema
        self.assertEqual(orders.combine_orders([70, 30, 10], 100), 2)

        # Caso com 5 requisições
        self.assertEqual(orders.combine_orders([50, 40, 30, 20, 10], 80), 3)

        # Caso onde todas são enviadas individualmente
        self.assertEqual(orders.combine_orders([100, 100], 100), 2)

        # Caso onde nenhuma combinação é possível
        self.assertEqual(orders.combine_orders([90, 80, 70], 100), 3)

    def test_all_requests_same(self):
        self.assertEqual(Orders().combine_orders([50, 50, 50], 100), 2)

    def test_requests_not_list(self):
        with self.assertRaises(InvalidOrderError):
            Orders().combine_orders("not_a_list", 100)

    def test_request_exceeds_n_max(self):
        with self.assertRaises(BusinessRuleError):
            Orders().combine_orders([150], 100)  # Requisição maior que n_max
