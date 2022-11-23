#!/usr/bin/env python3
"""
created: 2022-11-23
@author: seraph1001100
"""

from account import Account


class ChequingAccount(Account):
    """Savings Account Class"""
    def __init__(self, account_holder_name, current_balance):
        super().__init__(account_holder_name, current_balance)
        self._overdraft_limit = 500
        self._rate_of_interest = .01

    def withdraw(self, amount):
        """This function withdraws funds from current_balance if funds are available."""
        if self._current_balance <= 0 and amount > self._overdraft_limit:
            return False
        elif self._current_balance > 0 and amount > self._current_balance + self._overdraft_limit:
            return False
        else:
            self._current_balance -= amount
            return True
