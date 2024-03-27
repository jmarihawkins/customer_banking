# customer_banking.py
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Prompt the user to set the savings account details
    savings_balance = float(input("Enter savings balance: "))
    savings_interest_rate = float(input("Enter savings interest rate (%): "))
    savings_months = int(input("Enter months for savings account: "))

    # Call the create_savings_account function and pass in user input
    savings_updated_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest_rate, savings_months
    )

    # Print out the interest earned and updated savings account balance with interest earned
    print(f"Savings interest earned: ${savings_interest_earned:.2f}")
    print(f"Updated savings balance: ${savings_updated_balance:.2f}")

    # Prompt the user to set the CD account details
    cd_balance = float(input("Enter CD balance: "))
    cd_interest_rate = float(input("Enter CD interest rate (%): "))
    cd_months = int(input("Enter months for CD account: "))

    # Call the create_cd_account function and pass in user input
    cd_updated_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest_rate, cd_months
    )

    # Print out the interest earned and updated CD account balance with interest earned
    print(f"CD interest earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD balance: ${cd_updated_balance:.2f}")

if __name__ == "__main__":
    main()