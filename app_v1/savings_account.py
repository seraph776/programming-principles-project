#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
"""

from account import Account
from colorz import Colorz


class SavingsAccount(Account):
    def __init__(self, account_holder_name, current_balance):
        super().__init__(account_holder_name, current_balance)
        self._minimum_balance = 200
        self._rate_of_interest = .05

    def withdraw(self, amount):
        if amount > self._current_balance - self._minimum_balance:
            print(Colorz.red(f'Error! That amount would exceed your minimum balance of ${self._minimum_balance}'))
            return False
        else:
            self._current_balance -= amount
            print(f'Current Balance: {self._current_balance}')
            return True

