# savings_account.py
from Accounts import Account

def create_savings_account(balance, interest, months):
    account = Account(balance, 0)
    interest_earned = balance * (interest / 100) * (months / 12)
    updated_balance = balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)
    return account.balance, account.interest