# cd_account.py
from accounts import Account

def create_cd_account(balance, interest_rate, months):
    # Create an instance of the Account class and pass in the parameters
    cd_account = Account(balance)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated balance to the set_balance method using the instance of the Account class
    cd_account.set_balance(updated_balance)

    # Pass the interest earned to the set_interest method using the instance of the Account class
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return cd_account.balance, cd_account.interest