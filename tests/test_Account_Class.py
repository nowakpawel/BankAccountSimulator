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
        self.assertEqual(self.acc.balance, 0, msg="Balance should 0 when object is initialized.")

    def test_deposit(self):
        self.acc.deposit(1000)

        self.assertEqual(self.acc.balance, 1000, msg="Account's balance should be increased.")

    def test_withdraw_empty_balance(self):
        self.assertEqual(self.acc.withdraw(1000), "Your account balance is not enough", msg="Should not be possibility to withdraw.")

    def test_show_balance(self):
        self.acc.deposit(2500.55)

        self.assertEqual(self.acc.show_balance(), 2500.55, msg="Method should show current account balance.")
