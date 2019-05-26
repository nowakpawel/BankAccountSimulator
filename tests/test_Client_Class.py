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