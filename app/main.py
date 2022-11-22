#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
project: 
"""

from bank import Bank
from application import Application
from savings_account import SavingsAccount
from chequing_account import CheckingAccount

a1 = SavingsAccount(123, 'jon', )
a2 = CheckingAccount(103,'amy')

bank = Bank()
bank.add_account(a1)
bank.add_account(a2)


search = bank.search_account(123)
print(search)



