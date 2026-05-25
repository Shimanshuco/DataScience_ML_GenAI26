# List Comprehension
# List comprehension is a concise way to create lists in Python. 
# It allows you to generate a new list by applying an expression to each item in an iterable, optionally filtering items using a condition.

# Basic Syntax:
# new_list = [expression for item in iterable if condition]

# Advantages of List Comprehension:
    #  1. Conciseness: List comprehensions can often replace multiple lines of code with a single line, making it more concise and easier to read.
    #  2. Readability: Many developers find list comprehensions more readable than traditional loops, especially for simple transformations and filtering.
    #  3. Performance: List comprehensions can be faster than traditional loops for creating lists, as they are optimized for this specific use case.

# Add 1 to 10 numbers to a list 
# Using a for loop
num=[]
for i in range(1,11):
    num.append(i)
print(num)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using List Comprehension
num = [i for i in range(1,11)]
print(num)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Scalar Multiplication on a vector
vector = [1,2,3]
scalar = 2  
# Using a for loop
for i in range(len(vector)):
    vector[i] = vector[i] * scalar
print(vector)   # [2, 4, 6]

# Using List Comprehension
vector = [1,2,3]
scalar = 2
vector = [x * scalar for x in vector]

# Add squares
l = [1,2,3,4] # => [1,4,9,16]
#Using for loop
for i in range(len(l)):
    l[i]=l[i]*l[i];
print(l)

# Using List Comprehension
l=[1,2,3,4]
l = [x*x for x in l]
print(l)

# Print all number divisble by 5 in range of 1 to 50
list = [i for i in range(1,51)];
print(list)

div_by_5 = [i for i in list if i%5==0]
print(div_by_5)


# Find languages that start with p
lang = ['php','java','python','javascript','c']
#for loop
for i in lang:
    if(i[0]=='p'):
        print(i);
        
p_lang = [i for i in lang if i[0]=='p']
print(p_lang)

# Nested if with list comprehension
basket = ['apple','kiwi','banana','cherry','mango']
my_fruits = ['apple','banana','mango']

a_fruits = [i for i in my_fruits if i in basket if i.startswith('a')]
print(a_fruits)

# Print 3*3 matrix using list comprehension
matrix=[[i for i in range(1,4)] for j in range(3)]
# Working of above code:
# 1. The outer list comprehension iterates over a range of 3 (for j in range(3)), which means it will create 3 rows in the matrix.
# 2. For each iteration of the outer loop, the inner list comprehension (i for i in range(1,4)) generates a list of numbers from 1 to 3, which will be the columns of the matrix.
print(matrix)   # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


# Cartesian Product of two lists using list comprehension
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = [(x,y) for x in list1 for y in list2]
print(cartesian_product)   # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

# 2 ways to traverse a list using list 

# 1. itemwise
my_list = ['a', 'b', 'c']
for item in my_list:
    print(item)

# 2. indexwise
my_list = ['a', 'b', 'c']
for i in range(len(my_list)):
    print(my_list[i])