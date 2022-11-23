#!/usr/bin/env python3
"""
created: 2022-11-23
@author: seraph1001100
"""

from savings_account import SavingsAccount
from chequing_account import ChequingAccount


class Bank:
    def __init__(self):
        self._available_accounts = []

    def add_account(self, account):
        self._available_accounts.append(account)

    def view_all_accounts(self):
        return self._available_accounts

    def open_new_account(self):
        print('Please select the type of account you want to open (1-2)')
        print('1 - Savings')
        print('2 - Chequing')

        while True:
            user_choice = input('> ')
            if not user_choice.isdigit() or int(user_choice) not in [1, 2]:
                print('Invalid input!')
                continue
            else:
                break

        while True:
            user_choice = input('> ')
            if not user_choice.isdigit() or int(user_choice) not in [1, 2]:
                print('Invalid input!')
                continue
            else:
                break

        account_type = user_choice
        account_holder_name = input('Please enter your name:\n> ')

        if account_type == 'Savings':
            self.add_account(SavingsAccount(account_holder_name, 0))
        else:
            self.add_account(ChequingAccount(account_holder_name, 0))
        print(f'{account_type} account has been added to available Bank accounts')

    def search_account(self, account_number):
        """This function searches, and returns the account_number being requested.
        If the account cannot be found the function returns False."""
        available_accounts = [a._account_number for a in self._available_accounts]
        if account_number not in available_accounts:
            print('Account could not be found!')
            return False
        for account in self._available_accounts:
            if account_number == account._account_number:
                return account
