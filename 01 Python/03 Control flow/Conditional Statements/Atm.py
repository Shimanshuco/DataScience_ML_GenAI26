# Atm machine

menu = """
Welcome to the ATM machine
1. Check Balance
2. Deposit
3. Withdraw
5. Pin Change
6. Exit
"""

user_name = input("Enter your name: ")
balance = 1000
pin = "1234"
action = int(input(menu))

if(action == 1):
    print("Your balance is: ", balance)
elif(action == 2):
    deposit = int(input("Enter the amount to deposit: "))
    balance += deposit
    print("Amount deposited successfully")
elif(action == 3):
    withdraw = int(input("Enter the amount to withdraw: "))
    if(withdraw <= balance):
        balance -= withdraw
        print("Amount withdrawn successfully")
    else:
        print("Insufficient balance")
elif(action == 5):
    old_pin = input("Enter your old pin: ")
    if(old_pin == pin):
        new_pin = input("Enter your new pin: ")
        pin = new_pin
        print("Pin changed successfully")
    else:
        print("Invalid old pin")
elif(action == 6):
    print("Thank you for using the ATM machine")
else:
    print("Invalid action")