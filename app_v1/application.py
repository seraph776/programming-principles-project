#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
"""
import sys
import time
from colorz import Colorz
from bank import Bank
from savings_account import SavingsAccount
from chequing_account import ChequingAccount
import application_logger


class Application:
    def __init__(self, bank_application):
        self._menu_items = {1: 'Open Account', 2: 'Select Account', 3: 'Exit'}
        self.bank_application = bank_application

    def show_main_menu(self):
        while True:
            print(Colorz.cyan('------- MAIN MENU ------'))
            for idx, item in self._menu_items.items():
                print(f'\t{idx} - {item}')
            print('Please make a selection (1-3)')
            while True:
                user_input = input('> ')
                if not user_input.isdigit() or int(user_input) not in [1, 2, 3]:
                    print(Colorz.red('Invalid Input.\nPlease select (1-3)'))
                    continue
                else:
                    break
            user_input = int(user_input)
            if user_input == 1:
                self.bank_application.open_new_account()
            elif user_input == 2:
                available_accounts = [a._account_number for a in self.bank_application._available_accounts]
                print(Colorz.green(f'>>> Available accounts: {available_accounts}'))
                while True:
                    get_account_number = input('Enter account number:\n> ')
                    if not get_account_number.isdigit() or int(get_account_number) not in available_accounts:
                        print(Colorz.red('>>> Account number could not verified, please try again!'))
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

    def show_account_menu(self, account):

        while True:
            menu_items = {1: 'Check Balance', 2: 'Deposit', 3: 'Withdraw', 4: 'Exit Account'}
            print(Colorz.cyan(f'------- {account.class_type} #{account._account_number} MENU -------'))
            print(Colorz.yellow(f'>>> You have selected {account.class_type} #{account._account_number}:'))
            print(f'{Colorz.orange(account)}')
            for idx, item in menu_items.items():
                print(f'\t{idx} - {item}')
            print('Please make a selection (1-4)')
            while True:
                user_input = input('> ')
                if not user_input.isdigit() or int(user_input) not in [1, 2, 3, 4]:
                    print(Colorz.red('Invalid Input.\nPlease select (1-4)'))
                    continue
                else:
                    break
            selection = menu_items.get(int(user_input))
            if selection == 'Check Balance':
                print(Colorz.green(f'>>> Account Balance: ${account._current_balance:.2f}'))
                application_logger.logging.info(f'Account Balance: ${account._current_balance:.2f}')
                time.sleep(2)
                continue
            elif selection == 'Deposit':
                while True:
                    amount = input('Enter amount that you wish to deposit:\n> ')
                    if not amount.isdigit():
                        print(Colorz.red('Invalid Input, digits only!'))
                        continue
                    else:
                        break

                account.deposit(int(amount))
                print(Colorz.green(
                    f'>>> ${amount} has been deposited. Your current balance is now: ${account._current_balance:.2f} '))
                application_logger.logging.info(f'$ {amount:.2f} has been deposited into account #{account._account_number}. Available balance ${account._current_balance:.2f}')
                time.sleep(2)
            elif selection == 'Withdraw':
                while True:
                    amount = input('Enter amount that you wish to withdraw:\n> ')
                    if not amount.isdigit():
                        print(Colorz.red('Invalid Input, digits only!'))
                        continue
                    application_logger.logging.info(f'${amount} has been withdrawn from account #{account._account_number}. Available balance ${account._current_balance:.2f}')
                    if not account.withdraw(int(amount)):
                        continue
                    else:
                        break
            elif selection == 'Exit Account':
                self.show_main_menu()

    def run(self):
        print(Colorz.green('Loading account list with three (3) ChequingAccount instances and three (3) SavingsAccount instances ...\n'))
        time.sleep(3)

        # Define a constructor that populates the account list with hardcoded of three
        # ChequingAccount instances and three SavingsAccount instances
        chequing_1 = ChequingAccount('smith', 1000)
        chequing_2 = ChequingAccount('johnson', 1000)
        chequing_3 = ChequingAccount('williams', 1000)
        savings_v1 = SavingsAccount('jones', 1000)
        savings_v2 = SavingsAccount('miller', 1000)
        savings_v3 = SavingsAccount('davis', 1000)
        accounts_list = [chequing_1, chequing_2, chequing_3, savings_v1, savings_v2, savings_v3]
        for account in accounts_list:
            self.bank_application.add_account(account)
            application_logger.logging.info(f'Adding {account.class_type} # {account._account_number} to Banking application')
        print(Colorz.green('Testing Account "account_holder_name" setter method...'))
        time.sleep(2)
        before = chequing_1.account_holder_name
        chequing_1.account_holder_name = 'seraph'
        print(f'{before.title()} has been updated to {chequing_1.account_holder_name.title()}!\n')
        time.sleep(2)

        print(Colorz.green('Testing Account "rate_of_interest" setter method...'))
        time.sleep(2)
        before = chequing_1.rate_of_interest
        chequing_1.rate_of_interest = 7.76
        print(f'Rate of Interest has been updated from {before} to {chequing_1.rate_of_interest}!\n')
        time.sleep(2)
        print(Colorz.green('Now Testing main function...'))
        time.sleep(2)

        self.show_main_menu()
