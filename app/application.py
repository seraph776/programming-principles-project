#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
"""


import sys
import bank


class Application:
    def __init__(self, bank_application):
        self._menu_items = {1: 'Open Account', 2: 'Select Account', 3: 'Exit'}
        self.bank_application = bank_application

    def show_main_menu(self):
        while True:
            for idx, item in self._menu_items.items():
                print(f'{idx} - {item}')
            print('Please make a selection (1-3)')
            while True:
                user_input = input('> ')
                if not user_input.isdigit() or int(user_input) not in [1, 2, 3]:
                    print('Invalid Input.\nPlease select (1-3)')
                    continue
                else:
                    break
            user_input = int(user_input)
            if user_input == 1:
                self.bank_application.open_new_account()
            elif user_input == 2:
                print('Please select enter your account number')

                while True:
                    get_account_number = input('Enter account number\n> ')
                    if int(get_account_number) not in self.bank_application.available_accounts:
                        print('Account number could not be found')
                        continue
                    elif int(get_account_number) in self.bank_application.available_accounts:
                        self.show_account_menu()

    def show_account_menu(self):
        menu_items = {1: 'Check Balance', 2: 'Deposit', 3: 'Withdraw', 4: 'Exit Account'}
        for idx, item in menu_items.items():
            print(f'{idx} -{item}')
        print('Please make a selection (1-4)')
        while True:
            user_input = input('> ')
            if not user_input.isdigit() or int(user_input) not in [1, 2, 3, 4]:
                print('Invalid Input.\nPlease select (1-4)')
                continue
            else:
                break
        user_input = input(user_input)
        if int(user_input) == 1:
            print(f'{self.bank_application}')

    def run(self):
        self.show_main_menu()
