#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
"""
from account import Account


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder_name, current_balance):
        super().__init__(account_number, account_holder_name, current_balance)
        self._overdraft_limit = 500
        self._rate_of_interest = .01


    def withdraw(self, amount):
        if self._current_balance + self._overdraft_limit >= amount:
            self._current_balance -= amount
        else:
            return f'Error! ${amount} exceeds your current balance ${self._current_balance} and overdraft limit of ${self._overdraft_limit}!'


