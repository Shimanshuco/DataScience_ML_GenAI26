# input() : A built-in function used to read user input from the console.
# It takes an optional prompt string as an argument and returns the input as a string.
name = input("Enter your name: ")  # Prompts the user to enter their name and stores it in the variable 'name'.
print("Hello, " + name + "!")  # Outputs a greeting message that includes the

# user input stored in the variable 'name'.
# Example of using input() to read a number and perform a calculation
num1 = input("Enter the first number: ")  # Reads the first number as a string
num2 = input("Enter the second number: ")  # Reads the second number as a string
# Calculation 
sum = num1 + num2  # This will concatenate the two strings instead of adding them as numbers
print(type(num1), type(num2) , type(sum))  # Outputs: <class 'str'>, confirming that num1 and num2 are strings
print("The sum of the two numbers is: " + sum)  # Outputs the concatenation

# Correct way to perform the calculation by converting the input strings to integers
num1 = int(input("Enter the first number: "))  # Reads the first number and converts it to an integer
num2 = int(input("Enter the second number: "))  # Reads the second number and converts it to an integer
sum = num1 + num2  # Now this will correctly add the two numbers
print("The sum of the two numbers is: " + str(sum))  # Outputs the sum as a string
print(type(sum))  # Outputs: <class 'int'>, confirming that sum is an integer

# Syntax of input() function:
# input(prompt)
# - prompt: A string that is displayed to the user before they enter their input. This is optional.

# Why python takes string as default input?
# String is most universal data type that can represent a wide range of inputs, including numbers, text, and special characters. 
# By treating all input as strings, Python allows for greater flexibility in handling user input without making assumptions about 
# the data type. 
# Easy type conversion from string to other data types (like int, float, etc.) can be done using built-in functions, 
# giving developers control over how to interpret the input.

a = "5";
b = "10";
print(a + b)  # This will output "510" because a and b are strings, and the + operator concatenates them.

#Type conversion 


a = int(a)  # Convert string '5' to integer 5
b = int(b)  # Convert string '10' to integer 10
print(a + b)  # This will output 15 because a and b are now integers, and the + operator performs addition.
