# Make a menu driven calculator using if-else.

print("Welcome to the calculator")
print("--------------------------")
fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))
op = input("Enter the operator (+, -, *, /) : ")

if(op=="+"):
    print("The sum is : ",fnum+snum);
elif(op=="-"):
    print("The difference is : ",fnum-snum);
elif(op=="*"):
    print("The product is : ",fnum*snum);
elif(op=="/"):
    if(snum!=0):
        print("The quotient is : ",fnum/snum);
    else:
        print("Division by zero is not allowed");
else:
    print("Invalid operator");

print("Thank you for using the calculator")
print("--------------------------")