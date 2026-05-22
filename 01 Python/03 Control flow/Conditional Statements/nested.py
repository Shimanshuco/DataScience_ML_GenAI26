# Nested Conditional Statements
# A nested conditional statement is a conditional statement that is contained within another conditional statement.

num = int(input("Enter a number: "))

if(num > 0):
    print("The number is positive.")
    if(num % 2 == 0):
        print("The number is even.")
    else:
        print("The number is odd.")
elif(num < 0):
    print("The number is negative.")
else:
    print("The number is zero.")