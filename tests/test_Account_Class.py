from sources.Core import Account
import unittest


class AccountClassTestCase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("\n\n============ Running tests: ============\n\n")

    @classmethod
    def tearDownClass(cls):
        print("\n============ All tests executed ============")

    def setUp(self):
        self.acc = Account("Test", "Testowy")

    """===================================== TEST =========================================="""

    # def test_print_account_details(self):
    #     print ("Running " + self._testMethodName + "...", end="")
    #     self.assertEqual(self.acc.print_account_details(), "Owner: Test Testowy\nAccount Number: " +
    #                      self.acc.accountNumber + "\nBalance: 0", msg="Details must match")
    #     print("OK")

    def test_generate_account_number(self):
        print ("Running " + self._testMethodName + "...", end="")
        account_number = self.acc.generate_account_number()
        self.assertEqual(len(account_number), 24, msg="Account is not exactly 24 length.")
        print("OK")

    def test_balance(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.assertEqual(self.acc.balance, 0, msg="Balance should be 0 when object is initialized.")
        print("OK")

    def test_deposit(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.acc.deposit(1000)
        self.assertEqual(self.acc.balance, 1000, msg="Account's balance should be increased.")
        print("OK")

    def test_withdraw_empty_balance(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.assertEqual(self.acc.withdraw(1000), "Your account balance is not enough",
                         msg="Should not be possibility to withdraw.")
        print("OK")

    def test_withdraw(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.acc.deposit(5000)
        self.assertEqual(self.acc.withdraw(200.50), 4799.50, msg="Withdraw should be possible")
        print("OK")

    def test_show_balance(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.acc.deposit(2500.55)
        self.assertEqual(self.acc.show_balance(), 2500.55, msg="Method should show current account balance.")
        print("OK")


if __name__ == '__main__':
    unittest.main()