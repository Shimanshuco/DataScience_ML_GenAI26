# Reading a text file

# Using read() method
f = open('sample.txt','r') # Syntax : file_object = open('filename','mode')
s = f.read() # Syntax : variable_name = file_object.read(characters)
print(s)
f.close()

f = open('sample.txt','r')
s = f.read(5) # This will read the first 5 characters from the file.
print(s)
f.close()

# Using readline() method
f = open('sample.txt','r')
s = f.readline() # This will read the first line from the file.
print(s)
s = f.readline() # This will read the second line from the file.
print(s)
f.close()