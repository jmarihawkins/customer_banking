# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def get_valid_input(prompt):
    """Prompt the user for input, handle spaces and commas, and validate the input."""
    while True:
        user_input = input(prompt)
        cleaned_input = user_input.replace(' ', '').replace(',', '')  # Remove spaces and commas
        try:
            # Check if input contains only digits and at most one decimal point
            if not cleaned_input.replace('.', '', 1).isdigit():
                raise ValueError("Invalid input. Please enter a valid numerical value without letters or special characters.")
            # Check if there are multiple decimal points
            if cleaned_input.count('.') > 1:
                raise ValueError("Invalid input. Please enter a valid numerical value without multiple decimal points.")
            return float(cleaned_input)  # Convert cleaned input to float
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = get_valid_input("Enter savings balance: ")
    savings_interest = get_valid_input("Enter interest rate for savings (%): ")
    savings_maturity = int(get_valid_input("Enter number of months for savings: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings account interest earned: ${interest_earned_savings:.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = get_valid_input("Enter CD balance: ")
    cd_interest = get_valid_input("Enter interest rate for CD (%): ")
    cd_maturity = int(get_valid_input("Enter number of months for CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD account interest earned: ${interest_earned_cd:.2f}")
    print(f"Updated CD account balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()