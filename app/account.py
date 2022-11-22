#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
"""


class Account:
    def __init__(self, account_number, account_holder_name, current_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._current_balance = current_balance
        self._rate_of_interest = .03


    def __repr__(self):
        return f'{self.__class__.__name__}(accountNumber={self._account_number},' \
               f' accountHolderName={self._account_holder_name}, rateOfInterest={self._rate_of_interest}, ' \
               f'currentBalance={self._current_balance})'

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, new_name):
        self._account_holder_name = new_name
        print('Name has been changed!')

    @property
    def rate_of_interest(self):
        return self._rate_of_interest

    @rate_of_interest.setter
    def rate_of_interest(self, amount):
        self._rate_of_interest = amount

    def get_account_number(self):
        return self._account_number

    def get_account_holder_name(self):
        return self._account_holder_name

    def get_rate_of_interest(self):
        return self._rate_of_interest

    def get_current_balance(self):
        return self._current_balance

    def deposit(self, amount):
        self._current_balance += amount

    def withdraw(self, amount):
        if self._current_balance >= amount:
            self._current_balance -= amount
        else:
            return False
