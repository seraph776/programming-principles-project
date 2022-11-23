#!/usr/bin/env python3
"""
created: 2022-11-23
@author: seraph1001100
"""

import sys
from savings_account import SavingsAccount
from chequing_account import ChequingAccount
import random


class Application:
    """Application class"""

    def __init__(self, bank_application):
        """Initialize attributes"""
        self.bank_application = bank_application

    def show_main_menu(self):
        """Shows teh main menu of the application class"""
        while True:
            print('------- MAIN MENU ------')
            print('1 - Open Account')
            print('2 - Select Account')
            print('3 - Exit')
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
                available_accounts = [a._account_number for a in self.bank_application._available_accounts]
                print(f'>>> Available accounts: {available_accounts}')
                while True:
                    get_account_number = input('Enter account number:\n> ')
                    if not get_account_number.isdigit() or int(get_account_number) not in available_accounts:
                        print('>>> Account number could not verified, please try again!')
                        continue
                    else:
                        break

                while True:
                    get_account_number = int(get_account_number)
                    selected_account = \
                        [a for a in self.bank_application._available_accounts if
                         a._account_number == get_account_number][0]

                    self.show_account_menu(selected_account)
            elif user_input == 3:
                print('Goodbye!')
                sys.exit()

    def show_account_menu(self, selected_account):
        while True:
            print(f'------- {selected_account.class_type} #{selected_account._account_number} MENU -------')
            print(f'>>> You have selected {selected_account.class_type} #{selected_account._account_number}:')
            print(f'{selected_account}')
            print('1 - Check Balance')
            print('2 - Deposit')
            print('3 - Withdraw')
            print('4 - Exit Account')
            print('Please make a selection (1-4)')
            print('Please make a selection (1-4)')
            while True:
                user_input = input('> ')
                if not user_input.isdigit() or int(user_input) not in [1, 2, 3, 4]:
                    print('Invalid Input.\nPlease select (1-4)')
                    continue
                else:
                    break
            if user_input == 'Check Balance':
                print(f'>>> Account Balance: ${selected_account._current_balance:.2f}')
                continue
            elif user_input == 'Deposit':
                while True:
                    amount = input('Enter amount that you wish to deposit:\n> ')
                    if not amount.isdigit():
                        print('Invalid Input, digits only!')
                        continue
                    else:
                        break

                selected_account.deposit(int(amount))
                print(
                    f'>>> ${amount} has been deposited. Your current balance is now: ${selected_account._current_balance:.2f} ')
            elif user_input == 'Withdraw':
                while True:
                    amount = input('Enter amount that you wish to withdraw:\n> ')
                    if not amount.isdigit():
                        print('Invalid Input, digits only!')
                        continue
                    if not selected_account.withdraw(int(amount)):
                        continue
                    else:
                        break
            elif user_input == 'Exit Account':
                self.show_main_menu()

    def run(self):
        print('Loading account list with three (3) ChequingAccount and three (3) SavingsAccount instances ...\n')
        # Define a constructor that populates the account list with hardcoded of three
        # ChequingAccount instances and three SavingsAccount instances:

        chequing_1 = ChequingAccount('smith', random.randint(10000, 99999))
        chequing_2 = ChequingAccount('johnson', random.randint(10000, 99999))
        chequing_3 = ChequingAccount('williams', random.randint(10000, 99999))
        savings_v1 = SavingsAccount('jones', random.randint(10000, 99999))
        savings_v2 = SavingsAccount('miller', random.randint(10000, 99999))
        savings_v3 = SavingsAccount('davis', random.randint(10000, 99999))
        accounts_list = [chequing_1, chequing_2, chequing_3, savings_v1, savings_v2, savings_v3]
        for account in accounts_list:
            self.bank_application.add_account(account)

        self.show_main_menu()
