# Writing in a text file
# Case 1 : File is not createdor present in the directory
f = open('sample.txt','w') # Syntax : file_object = open('filename','mode')
f.write('Hello World') # Syntax : file_object.write('data')
f.close() # Syntax : file_object.close()
# f.write('Hello World') # This will give an error because the file is closed and we cannot write in a closed file.

f = open('sample.txt','w') # This will overwrite the existing data in the file because we are opening the file in write mode.
f.write('Hello Python') # This will overwrite the existing data in the file because we are opening the file in write mode.
f.close()

# Case 2 : Write multiline data in a text file
f = open('sample.txt','w')
f.write('Hello World\n') # \n is used to move to the next line
f.write('Hello Python\n')
f.write('Hello Data Science\n')
f.close()

# Case 3 : Already existing data in the file and we want to add new data without overwriting the existing data
f = open('sample.txt','w')
f.write('Hello , I am a Data Science Student.\n')
f.close()

# Probelm with 'w' mode : 
# If we want to add new data in the file without overwriting the existing data.

# Solution : We can use 'a' mode (append mode) to add new data in the file without overwriting the existing data.
f = open('sample.txt','a') # This will add new data in the file without overwriting the existing data because we are opening the file in append mode.
f.write('I am learning Python for Data Science.\n')
f.close()

# Write a list of data in a text file
my_list = ['Hello World\n','Hello Python\n','Hello Data Science\n']
f = open('sample.txt','a')
for item in my_list:
    f.write(item)
f.close()



# Probelm 
my_dict = {'name':'John','age':30,'city':'New York'}
f = open('sample.txt','a')
# f.write(my_dict) # This will give an error because we cannot write a dictionary in a text file directly.
f.write(str(my_dict)) # This will convert the dictionary into a string and then write it in the file.
f.close()

with open('sample.txt','a') as f: # This is a better way to handle files because it will automatically close the file after the block of code is executed.
    print(f.read())
    print(type(f.read())) # This will print the type of data read from the file. It will be a string because we are reading from a text file.