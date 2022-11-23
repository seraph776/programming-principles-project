#!/usr/bin/env python3
"""
created: 2022-11-23
@author: seraph1001100
"""

from bank import Bank
from application import Application


def main():
    bank = Bank()
    app = Application(bank).run()


if __name__ == '__main__':
    main()


