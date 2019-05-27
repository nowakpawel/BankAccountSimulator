"""
Simple program simulating bank account for practicing Python and Python's unit tests

Author: Pawel Nowak
e-mail: kontakt.nowakpawel@gmail.com

"""

from sources.Application import Application

running = True

while running:
    Application.print_actions()

    choose = int(input("Choose action\t"))

    if choose == sorted(Application.action_list.keys())[-1]:
        print("Good Bye")
        running = False

    if choose == 0 or choose > len(Application.action_list):
        print("Wrong option")
        continue

    Application.perform(choose)




