from sources.Core import Client
import unittest


class ClientClassTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n\nTesting: Client class tests cases\n")

    def setUp(self):
        self.client = Client("Pawel", "Nowak")

    def test_print_details(self):
        print("Running " + self._testMethodName + "...", end="")
        self.assertEqual(self.client.print_details(), "Name: Pawel\nLast Name: Nowak\nAccount Number: " +
                             self.client._account.accountNumber + "\nBalance: 0")

        print("OK")

    def test_deposit(self):
        print("Running " + self._testMethodName + "...", end="")
        self.assertTrue(self.client.deposit(1500.55))

        print("OK")

    def test_deposit(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.client.deposit(1000)
        self.assertEqual(self.client._account.balance, 1000, msg="Account's balance should be increased.")
        print("OK")

    def test_withdraw_empty_balance(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.assertEqual(self.client.withdraw(1000), "Your account balance is not enough",
                         msg="Should not be possibility to withdraw.")
        print("OK")

    def test_withdraw(self):
        print ("Running " + self._testMethodName + "...", end="")
        self.client.deposit(5000)
        self.assertEqual(self.client.withdraw(200.50), 4799.50, msg="Withdraw should be possible")
        print("OK")