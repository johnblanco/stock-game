import unittest
from game import update_account


class TestAccount(unittest.TestCase):
    def test_invalid_operation(self):
        account = {
            'cash': 900,
            'stocks': 0,
            'costs': 0,
            'value': 900
        }

        res = update_account(10, account, 'c10000')

        self.assertEqual(res, account)

    def test_initial_buy(self):
        account = {
            'cash': 900,
            'stocks': 0,
            'costs': 0,
            'value': 900
        }

        res = update_account(10, account, 'c10')

        self.assertEqual(800, res['cash'])
        self.assertEqual(10, res['stocks'])
        self.assertEqual(25, res['costs'])
        self.assertEqual(875, res['value'])

    def test_partial_sell(self):
        account = {
            'cash': 800,
            'stocks': 10,
            'costs': 25,
            'value': 875
        }

        res = update_account(10, account, 'v5')

        self.assertEqual(850, res['cash'])
        self.assertEqual(5, res['stocks'])
        self.assertEqual(50, res['costs'])
        self.assertEqual(850, res['value'])
