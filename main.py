"""
Simple program simulating bank account for practicing Python and Python's unit tests

Author: Paweł Nowak
e-mail: kontakt.nowakpawel@gmail.com

"""


from sources.Account import Account

testAccount = Account("Pawel", "Nowak")

testAccount.print_account_details()

account2 = Account("Natalia", "Cichocka")

account2.print_account_details()
print(account2.accounts_list)