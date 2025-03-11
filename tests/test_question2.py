import unittest

from src.question2 import Orders


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
