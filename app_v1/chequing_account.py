#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
"""
from account import Account
from colorz import Colorz


class ChequingAccount(Account):
    def __init__(self, account_holder_name, current_balance):
        super().__init__(account_holder_name, current_balance)
        self._overdraft_limit = 500
        self._rate_of_interest = .01

    def withdraw(self, amount):
        if self._current_balance <= 0 and amount > self._overdraft_limit:
            print('Insufficient funds')
        elif self._current_balance > 0 and amount > self._current_balance + self._overdraft_limit:
            print(Colorz.red(
                f'Error! ${amount} exceeds your current balance ${self._current_balance} and overdraft limit of ${self._overdraft_limit}!'))
            return False
        else:
            self._current_balance -= amount
            print(f'Current Balance: {self._current_balance} ')
            return True

