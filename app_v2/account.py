#!/usr/bin/env python3
"""
created: 2022-11-23
@author: seraph1001100
"""
import random


class Account:
    """Account class"""
    def __init__(self, account_holder_name, current_balance):
        """IInitialize attributes."""
        self.class_type = self.__class__.__name__
        self._account_number = random.randint(10000, 99999)
        self._account_holder_name = account_holder_name
        self._current_balance = current_balance
        self._rate_of_interest = .03

    def __repr__(self):
        """Returns the representation of the class object as a string """
        return f'{self.__class__.__name__}(accountNumber={self._account_number},' \
               f' accountHolderName={self._account_holder_name}, rateOfInterest={self._rate_of_interest}, ' \
               f'currentBalance={self._current_balance})'

    @property
    def account_holder_name(self):
        """account_holder_name is an attribute of Account class"""
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, new_name):
        """account_holder_name setter"""
        self._account_holder_name = new_name
        print('Account name has been updated.')

    @property
    def rate_of_interest(self):
        """rate_of_interest is an attribute of Account"""
        return self._rate_of_interest

    @rate_of_interest.setter
    def rate_of_interest(self, amount):
        """rate_of_interest setter"""
        self._rate_of_interest = amount

    def get_account_number(self):
        """Returns the account number"""
        return self._account_number

    def get_account_holder_name(self):
        """Returns the account holder's name"""
        return self._account_holder_name

    def get_rate_of_interest(self):
        """Returns the interest rate applied to teh account"""
        return self._rate_of_interest

    def get_current_balance(self):
        """Returns the current balance"""
        return self._current_balance

    def deposit(self, amount):
        """Deposits amount into teh current balance of the account"""
        self._current_balance += amount
        return True

    def withdraw(self, amount):
        """Withdraws amount from current_balance if funds are available"""
        if amount > self._current_balance:
            return False
        else:
            self._current_balance -= amount
            return True
