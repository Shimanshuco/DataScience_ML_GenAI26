# 1. list()
print(list('hello'))   # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))   # [1, 2, 3]
print(list({1, 2, 3}))   # [1, 2, 3] (order may vary due to set nature)
print(list({'a': 1, 'b': 2}))   # ['a', 'b'] (keys of the dictionary)

# 2. len()
list = [1, 2, 3, 4]
print(len(list))   # 4

# Adding Items in a List

# 3. append() : Adds a single item to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)   # [1, 2, 3, 4]
l1 = [1, 2, 3]
l1.append('Data') 
print(l1) # [1, 2, 3, 'Data'] # append() adds the entire string 'Data' as a single element to the list.

# 4. extend() : Adds all items of an iterable (like another list) to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)   # [1, 2, 3, 4, 5]
# [1, 2, 3, 'D', 'a', 't', 'a'] # extend() treats the string 'Data' as an iterable and adds each character as a separate element to the list.

l2 = [1, 2, 3]
l2.extend('Data')
print(l2)   # [1, 2, 3, 'D', 'a', 't', 'a'] # extend() treats the string 'Data' as an iterable and adds each character as a separate element to the list.

# 5. insert() : Inserts an item at a specified index. The first argument is the index, and the second argument is the item to be inserted.
my_list = [1, 2, 3]
my_list.insert(1, 10)   # Insert 10 at index 1
print(my_list)   # [1, 10, 2, 3]

# Editing Items in a List

# 1. With indexing
my_list = [1, 2, 3]
my_list[1] = 20   # Change the item at index 1 to 20
print(my_list)   # [1, 20, 3]

# 2. With slicing
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]   # Change the items from index 1 to 2 (2 and 3) to 20 and 30
print(my_list)   # [1, 20, 30, 4, 5]

# 6. index() : Returns the index of the first occurrence of a specified value. If the value is not found, it raises a ValueError.
my_list = [1, 2, 3, 2]
print(my_list.index(2))   # 1 (the index of the first occurrence of 2)
# print(my_list.index(4))   # This will raise a ValueError since 4

# Deletion of Items in a List

# 1. del statement : Deletes an item at a specified index or a slice of items.
my_list = [1, 2, 3, 4, 5]
del my_list[1]   # Delete the item at index 1 (which is 2)
print(my_list)   # [1, 3, 4, 5]

del my_list[1:3]   # Delete the items from index 1 to 2 (which are 3 and 4)
print(my_list)   # [1, 5]

# 2. remove() : Removes the first occurrence of a specified value. If the value is not found, it raises a ValueError.
my_list = [1, 2, 3, 2]
my_list.remove(2)   # Remove the first occurrence of 2
print(my_list)   # [1, 3, 2]
# my_list.remove(4)   # This will raise a ValueError since 4 is not in the list

# 3. pop() : Removes and returns an item at a specified index. If no index is specified, it removes and returns the last item in the list.
my_list = [1, 2, 3]
print(my_list.pop(1))   # 2 (removes and returns the item at index 1)
print(my_list)   # [1, 3]
print(my_list.pop())   # 3 (removes and returns the last item)
print(my_list)   # [1]

# 4. clear() : Removes all items from the list, leaving it empty.
my_list = [1, 2, 3]
my_list.clear()   # Clear all items from the list
print(my_list)   # [] (the list is now empty)

# Operations on Lists

# 1. Concatenation : You can concatenate two lists using the + operator.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)   # [1, 2, 3, 4, 5, 6]

# 2. Repetition : You can repeat a list a specified number of times using the * operator.
list1 = [1, 2, 3]
repeated_list = list1 * 3
print(repeated_list)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 3. Membership : You can check if an item is in a list using the in keyword.
my_list = [1, 2, 3]
print(2 in my_list)   # True
print(4 in my_list)   # False

# 4. Iteration : You can iterate over the items in a list using a for loop.
my_list = [1, 2, 3]
for item in my_list:
    print(item)   # This will print each item in the list on a new line

# 5. count() : Returns the number of occurrences of a specified value in the list.
my_list = [1, 2, 3, 2]
print(my_list.count(2))   # 2 (the number of times 2 appears in the list)
print(my_list.count(4))   # 0 (4 does not appear in the list)

# 6. sort() : Sorts the items of the list in ascending order by default. You can also specify a custom sorting order using the key parameter.
my_list = [3, 1, 2]
my_list.sort()   # Sort the list in ascending order
print(my_list)   # [1, 2, 3]

my_list = ['banana', 'apple', 'cherry']
my_list.sort()   # Sort the list in alphabetical order
print(my_list)   # ['apple', 'banana', 'cherry']

my_list = ['banana', 'apple', 'cherry']
my_list.sort(key=len)   # Sort the list by the length of the strings
print(my_list)   # ['apple', 'banana', 'cherry'] (sorted by length of the strings)

# sort() in reverse order
my_list = [3, 1, 2]
my_list.sort(reverse=True)   # Sort the list in descending order
print(my_list)   # [3, 2, 1]

# 7. sorted() : Returns a new sorted list from the items of the iterable. It does not modify the original list.
my_list = [3, 1, 2]
sorted_list = sorted(my_list)   # Get a new sorted list
print(sorted_list)   # [1, 2, 3]
print(my_list)   # [3, 1, 2] (the original list

# sorted() with a custom sorting order
my_list = ['banana', 'apple', 'cherry']
sorted_list = sorted(my_list, key=len)   # Get a new list sorted by the length of the strings
print(sorted_list)   # ['apple', 'banana', 'cherry'] (sorted by length of the strings)

# 8. reverse() : Reverses the items of the list in place.
my_list = [1, 2, 3]
my_list.reverse()   # Reverse the list in place
print(my_list)   # [3, 2, 1]

# 9. reversed() : Returns an iterator that accesses the given sequence in the reverse order. It does not modify the original list.
my_list = [1, 2, 3]
reversed_list = list(reversed(my_list))   # Get a new list in reverse order
print(reversed_list)   # [3, 2, 1]
print(my_list)   # [1, 2, 3] (the original list is unchanged)

# 10. copy() : Returns a shallow copy of the list.
my_list = [1, 2, 3]
copied_list = my_list.copy()   # Get a shallow copy of the list
print(copied_list)   # [1, 2, 3]
print(my_list)   # [1, 2, 3] (the original list is unchanged)

# 11. min() and max() : Returns the smallest and largest item in the list, respectively.
my_list = [3, 1, 2]
print(min(my_list))   # 1 (the smallest item in the list)
print(max(my_list))   # 3 (the largest item in the list)

# Zip and unzip lists
# zip() : Takes iterables (can be zero or more), aggregates them in a tuple, and returns an iterator of tuples.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))   # Zip the two lists together
print(zipped)   # [(1, 'a'), (2, 'b'), (3, 'c')]

# unzip the zipped list
unzipped = list(zip(*zipped))   # Unzip the list of tuples
print(unzipped)   # [(1, 2, 3), ('a', 'b', 'c')]

# sum() : Returns the sum of all items in the list.
my_list = [1, 2, 3]
print(sum(my_list))   # 6 (the sum of the items in the list)