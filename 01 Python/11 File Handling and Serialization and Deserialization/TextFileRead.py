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

# Loop 
f = open('sample.txt','r')
while True:    # while f.readline() != '': # This will check if the end of the file is reached or not.
    s = f.readline()
    if s == '':
        break
    print(s)
f.close()


# Using readlines() method
f = open('sample.txt','r')
s = f.readlines() # This will read all the lines from the file and return a list of lines.
print(s)
f.close()

# Moving within a file
f = open('sample.txt','r')
s = f.read(5) # This will read the first 5 characters from the file
print(s)
f.seek(0) # This will move the file pointer to the beginning of the file.
s = f.read(5) # This will read the first 5 characters from the file again.
print(s)
f.close()

# Load big files in chunks
big_L = ["Hello" for i in range(1000000)]

with open('big_file.txt','w') as f:
    for line in big_L:
        f.write(line + '\n')

with open('big_file.txt','r') as f:
    chunk_size = 1000
    while len(f.read(chunk_size)) > 0: # This will read the file in chunks of 1000 characters until the end of the file is reached.
        print(f.read(chunk_size),end='') # This will print the chunk of data read from the file. end='' is used to avoid adding a new line after each chunk is printed.
        f.read(chunk_size) # This will move the file pointer to the next chunk of data to be read.


# seek : seek(offset, whence) is a method used to change the position of the file pointer. The offset is the number of bytes to move the file pointer, and whence is the reference point from which to move the file pointer. The whence parameter can take the following values:
# 0 : This is the default value. It means that the offset is from the beginning of the file.
# 1 : It means that the offset is from the current position of the file pointer.
# 2 : It means that the offset is from the end of the file.
# tell : tell() is a method used to get the current position of the file pointer. It returns the number of bytes from the beginning of the file to the current position of the file pointer.

# Example of using seek and tell
f = open('sample.txt','r')
print(f.tell()) # This will print the current position of the file pointer, which is 0 at the beginning of the file.
s = f.read(5) # This will read the first 5 characters from the file.
print(f.tell()) # This will print the current position of the file pointer, which is 5 after reading 5 characters from the file.
f.seek(0) # This will move the file pointer to the beginning of the file.
print(f.tell()) # This will print the current position of the file pointer, which is 0 after moving the file pointer to the beginning of the file.
f.seek(10) # This will move the file pointer to the 10th byte from the beginning of the file.
print(f.tell()) # This will print the current position of the file pointer, which is
# 10 after moving the file pointer to the 10th byte from the beginning of the file.
f.close()