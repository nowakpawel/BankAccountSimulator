from sources.Core import Account
import unittest


class AccountClassTestCase(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        print("\n============ All tests executed ============")

    def setUp(self):
        self.acc = Account("Test", "Testowy")

    """===================================== TEST =========================================="""

    def test_generate_account_number(self):
        print ("Running " + self._testMethodName + "...", end="")
        account_number = self.acc.generate_account_number()
        self.assertEqual(len(account_number), 24, msg="Account is not exactly 24 length.")
        print("OK")

    def test_balance(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.assertEqual(self.acc.balance, 0, msg="Balance should be 0 when object is initialized.")
        print("OK")
