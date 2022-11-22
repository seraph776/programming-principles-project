# #!/usr/bin/env python3
# """
# created: 2022-11-21
# @author: seraph1001100
# project:
# """

import random
from savings_account import SavingsAccount
from chequing_account import CheckingAccount


class Bank:
    def __init__(self):
        self._available_accounts = []
        self._number_of_accounts = len(self._available_accounts)
        self._account_list =[i._account_number for i in self._available_accounts]

    def add_account(self, account):
        self._available_accounts.append(account)

    def view_all_accounts(self):
        return self._available_accounts

    def open_new_account(self):
        print('Please select the type of account you want to open (1-2)')
        available_account_types = {1:'Savings', 2:'Chequing'}
        for idx, item in available_account_types.items():
            print(f'{idx} - {item}')

        while True:
            user_choice = input('> ')
            if not user_choice.isdigit() or int(user_choice) not in [1,2]:
                print('Invalid input!')
                continue
            else:
                break

        account_type = available_account_types.get(int(user_choice))
        account_holder_name = input('Please enter your name:\n> ')
        account_number = random.randint(1000, 9999)

        if account_type == 'Savings':
            self.add_account(SavingsAccount(account_number, account_holder_name, 0))
        else:
            self.add_account(CheckingAccount(account_number, account_holder_name, 0))
        print(f'{account_type} account #{account_number} has been added to available Bank accounts')

    def search_account(self, account_number):
        if account_number not in self._account_list:
            print('Account could not be found!')


