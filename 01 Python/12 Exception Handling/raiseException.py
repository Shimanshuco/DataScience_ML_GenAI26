# raise Exception
# The raise statement is used to raise an exception in Python.
# It allows us to create our own exceptions and specify the error message that should be associated with

# Example : 
raise NameError("Trying ................")

# 1
raise ValueError("This is a custom error message for ValueError")

# 2
raise Exception("This is a custom error message for a generic exception")

# 3
raise TypeError("This is a custom error message for TypeError")

# 4
raise ZeroDivisionError("This is a custom error message for ZeroDivisionError")

# Benefit of using raise Exception: (if we have try except)
# 1. It allows us to create our own exceptions and specify the error message that should be associated with the exception.
# 2. It can be used to signal that an error has occurred in a specific part of the code, which can help with debugging and error handling.
# 3. It can be used to enforce certain conditions in the code, such as input validation, by raising an exception when the conditions are not met.       


# Example 
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0:
            raise ValueError("Withdrawal amount must be greater than zero")  # This will raise a ValueError if the withdrawal amount is not greater than zero
        if amount > self.balance:
            raise ValueError("Insufficient funds in the account")  # This will raise a ValueError if the withdrawal amount exceeds the balance
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

# Create a bank account with a balance of 1000
account = Bank(1000)
# Attempt to withdraw an amount greater than the balance
account.withdraw(1500)  # This will raise a ValueError with the message "Insufficient funds in the account"
account.withdraw(-500)  # This will raise a ValueError with the message "Withdrawal amount must be greater than zero"
account.withdraw(500)  # This will successfully withdraw 500 and print the remaining balance of 500
