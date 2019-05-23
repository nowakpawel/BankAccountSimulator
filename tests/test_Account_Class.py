from sources.Account import Account
from unittest import TestCase


class AccountClassTestCase(TestCase):
    def setUp(self):
        self.acc = Account("Test", "Testowy")

    def test_generate_account_number(self):
        account_number = self.acc.generate_account_number()

        self.assertEqual(len(account_number), 24, msg="Account is not exactly 24 length.")

    def test_deposit(self):
        self.assertEqual(self.acc.balance, 90, msg="Dupa")