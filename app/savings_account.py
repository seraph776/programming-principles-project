#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
project: 
"""

from account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder_name, current_balance):
        super().__init__(account_number, account_holder_name,current_balance)
        self._minimum_balance = 200
        self._rate_of_interest = .05

    def withdraw(self, amount):
        if self._current_balance - amount < self._minimum_balance:
            return f'Error! That amount would exceed your minimum balance of ${self._minimum_balance}'
        else:
            self._current_balance -= amount
