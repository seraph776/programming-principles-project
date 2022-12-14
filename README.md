<div align="center">

# Simple Banking Application



![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=flat&labelColor=black)
[![License](https://img.shields.io/github/license/seraph776/programming-principles-project?logo=github&color=green&labelColor=black)](https://github.com/seraph776/programming-principles-project/blob/main/contributing.md) [![Contribute](https://img.shields.io/badge/Contribute-black?&logo=github&logoColor=black&label=&flat&labelColor=yellow)](https://github.com/seraph776/programming-principles-project/blob/main/contributing.md) [![Report Bugs](https://img.shields.io/badge/Report%20Bugz-black?&logo=github&logoColor=black&label=&flat&labelColor=red)](https://github.com/seraph776/programming-principles-project/issues/new/choose)

![image](https://user-images.githubusercontent.com/72005563/203419565-e452350b-4471-41e9-ba54-e22a5d3b3231.png)

_Show your support and give this repo a_ ⭐

</div>  
  
## Summary

This is a programming assignment from `PROG 10004 – Programming Principles` course offered at `Sheridan College CA`.  


## Objective


<details>
<summary> 🎯 Click to view  </summary>


Using the Object-Oriented UML model provided, create an Object-Oriented program that creates a
simple banking application which allows the user to open an account, select an account to withdraw and
deposit money, check balance. The structure of the program:

![image](https://user-images.githubusercontent.com/72005563/203414340-c85e9f54-df78-4bcc-bfeb-a41c128f6170.png)




## Part I User Interaction

- ### Class Application
Define a method showMainMenu that loops to display the following options until the user
chooses to exit the application:

1. Open Account: allows the user to open a new account *To be implemented for Bonus
2. Select Account: this allows the user to enter the account number of the account they
want to work with. Upon searching the account successfully, the application will call the
method showAccountMenu to display the Account Menu as described next.
3. Exit: allows the user to exit the applicatio

Define a method showAccountMenu that loops to display the following options until the
user chooses to exit the Account Menu:

1. Check Balance: Display the balance of the selected account
2. Deposit: Prompt the user for an amount to deposit and perform the deposit using
the methods in account class.
3. Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal
using the methods in the account class.
4. Exit Account: go back to Banking Main Menu
o Define and call the method run() to show the main menu to the end user

## Part II Business Logic

- ### Class Account
Represents a bank account. It is the base class for classes SavingsAccount and
ChequingAccount. Define the class as per the details provided in the class diagram

- ### SavingsAccount Subclass

Extends the class Account to represent the savings accounts. This
account requires the account holder(s) to maintain a minimum balance in the account. Override the
method withdraw of the base class to reject the transactions that would bring the current balance of
the account below the minimum balance. 

- ### ChequingAccount Subclass
Extends the class Account to represent the chequing accounts. This
account allows overdrafts, i.e., the account holder(s) can withdraw an amount that is more than
their current balance. Generally, there is a fee associated with overdrafts, but this application will
not keep a track of the fee for the sake of simplicity.
Override the method withdraw of the base class to reject transactions that cannot be completed
even after using the overdraft limit. This means if an account has an overdraft limit of 5000 CAD,
the account holder is allowed to withdraw up to 5000 CAD more than the money they have in the
account.


- ### Bank Class
Implements the business logic required for the banking. Keeps track of all the
accounts. Allows the user to open a new account or to search for an existing account. The class shall
define a List of Account objects. The list is to be populated with instances of SavingsAccount /
ChequingAccount
1.  Define a constructor that populates the account list with hardcoded of three
ChequingAccount instances and three SavingsAccount instances.
2. Define and implement the searchAccount() method that accepts an account number as
parameter. The method should find and return the account with matching account number
from the list of accounts. This method is to be used by Application to retrieve an account
using the account number entered by the user and perform transactions on the account.
3. Define a method openAccount

## Part III (10%) Error Handling. 

Using standard error checking (if-else) as well as exception handling (try-
except) to ensure the user input is valid both in terms of range and type of data entered. The application
should not crash at any point due to data input / processing. If recovery from the error(s) is not possible,
inform the user about the error and terminate the application. Examples:
- Negative values for withdrawal/deposit amounts should not be allowed.
- If conversion of the user input to a number of fails, the code should handle the exception.

**The program also included logging.**


</details>

## Requirements

This project was built using the Python `3.10.1`.

## Setup Instructions

Instructions on how to create a `pipenv` virtual environment.


<details>
<summary>⚙️  Click to View </summary>

1. Download [zip file](https://github.com/seraph776/programming-principles-project/archive/refs/heads/main.zip) 
2. Extract zip files
3. Change directory into projectFolder:

```
$ cd projectFolder
```

4. Install from Pipfile:

```
$ pipenv install  
```

5. Run the application from within virtual environment:

```
$ pipenv run python app/main.py
```

</details>



## Contact me
- **Email**: [seraph776@gmail.com](mailto:seraph776@gmail.com)


## License

[MIT](https://github.com/seraph776/programming-principles-project/blob/main/LICENSE) © [Seraph★776](https://github.com/seraph776) 
