# if-elif-else : The if-elif-else statement is used to execute a block of code if a specified condition is True, and another block of code if the condition is False. It can also be used to check multiple conditions.

user_name = input("Enter your name : ")
password = input("Enter your password : ")

if(password=="admin"):
    print("Welcome Admin ",user_name);
elif(password=="user"):
    print("Welcome User ",user_name);
else:
    print("Invalid password");