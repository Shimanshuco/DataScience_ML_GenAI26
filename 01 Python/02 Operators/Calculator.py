# User Enter 3 digit number we need to find sum of 3 digit number

num = int(input("Enter 3 digit number: "))
sum  = 0
first_digit = num //100;
second_digit = (num % 100) // 10
third_digit = num % 10

sum = first_digit + second_digit + third_digit
print("Sum of 3 digit number is: ", sum)