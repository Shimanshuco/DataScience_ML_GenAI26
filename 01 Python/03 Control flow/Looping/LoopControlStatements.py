# Loop control statements are used to control the flow of a loop. They are used to skip the current iteration of a loop, or to exit the loop completely.
# The three loop control statements in Python are:
# 1. break: This statement is used to exit the loop completely. When the break
    # statement is executed, the loop is terminated and the program continues with the next statement after the loop.
# 2. continue: This statement is used to skip the current iteration of the loop and
    # move to the next iteration. When the continue statement is executed, the rest of the code inside the loop is skipped for the current iteration, and the loop proceeds to the next iteration.
# 3. pass: This statement is used as a placeholder for code that is not yet implemented. It does nothing and is used when a statement is required syntactically but no action is needed.

# Example of break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Output: 1 2 3 4

# Example of continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Output: 1 2 3 4 6 7 8 9 10

# Example of pass statement
for i in range(1, 11):
    if i == 5:
        pass
    print(i)
# Output: 1 2 3 4 5 6 7 8 9 10

