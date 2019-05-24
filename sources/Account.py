import random


class Account:

    accounts_list = []

    def __init__(self, first_name, last_name, balance = 0):
        self.clientFirstName = first_name
        self.clientLastName = last_name
        self.accountNumber = self.generate_account_number()
        self.balance = balance

    # Implement destructor
    def __del__(self):
        print ("Object destroyed")

    def print_account_details(self):
        print("Owner: {} {}\nAccount Number: {}\nBalance: {}".format(self.clientFirstName, self.clientLastName, self.accountNumber, self.balance))

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

