import unittest

from exceptions import BusinessRuleError, InvalidContractError
from questions import Contract, Contracts


class TestContracts(unittest.TestCase):
    def test_get_top_N_open_contracts(self):
        contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5),
        ]
        renegotiated = [3]
        top_n = 3
        expected = [5, 4, 2]
        self.assertEqual(
            Contracts().get_top_N_open_contracts(contracts, renegotiated, top_n),
            expected,
        )

    def test_all_renegotiated(self):
        contracts = [Contract(1, 100)]
        renegotiated = [1]
        top_n = 1
        self.assertEqual(
            Contracts().get_top_N_open_contracts(contracts, renegotiated, top_n), []
        )

    def test_top_n_zero(self):
        self.assertEqual(
            Contracts().get_top_N_open_contracts([Contract(1, 100)], [1], 0), []
        )

    def test_invalid_contract_id(self):
        with self.assertRaises(InvalidContractError):
            Contract("abc", 100)  # ID não é inteiro

    def test_negative_debt(self):
        with self.assertRaises(BusinessRuleError):
            Contract(1, -50)  # Dívida negativa

    def test_top_n_negative(self):
        with self.assertRaises(InvalidContractError):
            Contracts().get_top_N_open_contracts([Contract(1, 100)], [], -1)
