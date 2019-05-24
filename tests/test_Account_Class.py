from sources.Account import Account
from unittest import TestCase


class AccountClassTestCase(TestCase):
    def setUp(self):
        self.acc = Account("Test", "Testowy")

    def tearDown(self):
        print("Tests completed")

    def test_generate_account_number(self):
        account_number = self.acc.generate_account_number()

        self.assertEqual(len(account_number), 24, msg="Account is not exactly 24 length.")

    def test_balance(self):
        self.assertEqual(self.acc.balance, 0, msg="Balance should 0 when object is initialized")

    def test_deposit(self):
        self.acc.deposit(1000)

        self.assertEqual(self.acc.balance, 1000, msg="Account's balance should be increased")
