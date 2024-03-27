# Overview

This project aims to create a customer banking system that enables users to manage savings and CD (Certificate of Deposit) accounts. Users can input account details such as balance, interest rates, and duration, and the system will calculate interest earned and update account balances accordingly.

# Files Summary

1. Accounts.py: Contains the Account class with methods for setting balance and interest.

2. savings_account.py: Implements the create_savings_account function. This function creates a savings account instance, calculates interest earned based on user input, updates the account balance with earned interest, and returns the updated balance and interest earned.

3. cd_account.py: Implements the create_cd_account function. This function creates a CD account instance, calculates interest earned based on user input, updates the account balance with earned interest, and returns the updated balance and interest earned.

4. customer_banking.py: Implements the main functionality. It imports create_savings_account and create_cd_account functions, prompts users to input account details, calls the appropriate functions to calculate interest and update balances, and displays the results.

# Functionality Summary

Functionality Summary:

1. create_savings_account(balance, interest_rate, months):
    - Imports the Account class from Accounts.py.
    - Creates an instance of Account with provided balance and interest rate.
    - Calculates interest earned based on provided parameters.
    - Updates savings account balance with interest earned.
    - Returns updated balance and interest earned.

2. create_cd_account(balance, interest_rate, months):
    - Imports the Account class from Accounts.py.
    - Creates an instance of Account with provided balance.
    - Calculates interest earned based on provided parameters.
    - Updates CD account balance with interest earned.
    - Returns updated balance and interest earned.

3. Main Function (customer_banking.py):
    - Imports create_savings_account and create_cd_account functions.
    - Prompts users to input savings and CD account details.
    - Calls respective functions to calculate interest and update balances.
    - Displays interest earned and updated account balances for both accounts.
    - Executes the program.
