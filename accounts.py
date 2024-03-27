# Accounts.py

class Account:
    def __init__(self, balance=0, interest=0):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest