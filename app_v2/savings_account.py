#!/usr/bin/env python3
"""
created: 2022-11-23
@author: seraph1001100
"""

from account import Account


class SavingsAccount(Account):
    """Savings Account Class"""
    def __init__(self, account_holder_name, current_balance):
        """Initialize attributes."""
        super().__init__(account_holder_name, current_balance)
        self._minimum_balance = 200  # This is an arbitrary amount; however standard with most accounts.
        self._rate_of_interest = .05

    def withdraw(self, amount):
        """This function withdraws funds from current_balance if funds are available."""
        if amount > self._current_balance - self._minimum_balance:
            return False
        else:
            self._current_balance -= amount
            return True
