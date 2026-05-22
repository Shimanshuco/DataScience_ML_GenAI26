#print number from 1 to a-1
a = int(input("Enter a number: "))
for i in range(1,a):
    print(i)

# range(start, stop, step)
# print even number from 1 to a-1
for i in range(2,a,2):
    print(i)

# print odd number from 1 to a-1
for i in range(1,a,2):
    print(i)

# print number from a-1 to 1
for i in range(a-1,0,-1):
    print(i)


