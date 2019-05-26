import random


class Account:

    accounts_list = []

    def __init__(self, first_name, last_name, balance=0):
        self.clientFirstName = first_name
        self.clientLastName = last_name
        self.accountNumber = self.generate_account_number()
        self.balance = balance
        self.history = [] # will contain operations history

    def generate_account_number(self):
        """
        Assumptions:
        - Account number has a 24 random digits
        - account Numbers can not duplicate
        :return: @accountNumber
        """
        account_number = ''
        generate_active = True

        while generate_active:
            while len(account_number) < 24:
                digit = random.randrange(0, 9)
                account_number += str(digit)

            if account_number not in self.accounts_list:
                self.accounts_list.append(account_number)
                generate_active = False

        return account_number


class Client:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._account = Account(first_name, last_name)

    def print_details(self):
        return "Name: {}\nLast Name: {}\nAccount Number: {}\nBalance: {}".format(self._first_name, self._last_name, self._account.accountNumber, self._account.balance)

    def deposit(self, amount):
        self._account.balance += amount

        return True

    def balance(self):
        return self._account.balance

    def deposit(self, amount):
        self._account.balance += amount

    def withdraw(self, amount):
        if amount > self._account.balance:
            return "Your account balance is not enough"
        else:
            self._account.balance -= amount

            return self._account.balance
