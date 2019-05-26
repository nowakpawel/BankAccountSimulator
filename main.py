"""
Simple program simulating bank account for practicing Python and Python's unit tests

Author: Pawel Nowak
e-mail: kontakt.nowakpawel@gmail.com

"""

from sources.Core import Client

client = Client("Pawel", "Nowak")
print(client.print_details())

client.deposit(1000)

print(client.print_details())




