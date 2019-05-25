import random


class Account:

    accounts_list = []

    def __init__(self, first_name, last_name, balance = 0):
        self.clientFirstName = first_name
        self.clientLastName = last_name
        self.accountNumber = self.generate_account_number()
        self.balance = balance
        self.history = [] # will contain operations history



    def print_account_details(self):
        return "Owner: {} {}\nAccount Number: {}\nBalance: {}".format(self.clientFirstName, self.clientLastName,
                                                                      self.accountNumber, self.balance)

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

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Your account balance is not enough"
        else:
            self.balance -= amount

            return self.balance

    def show_balance(self):
        return self.balance
