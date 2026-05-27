# Binary Files read
with open("schema.png", "rb") as f: # rb : read binary mode
    data = f.read() # This will read the binary data from the file and store it in the variable 'data'
    print(data) # This will print the binary data in the console. The output will be in bytes format.

# Modes of Binary Files:
# 'rb' : read binary mode
# 'wb' : write binary mode
# 'ab' : append binary mode
# 'rb+' : read and write binary mode
# 'wb+' : write and read binary mode

# Binary Files write
with open("bin.bin", "wb") as f: # wb : write binary mode
    data = b'Hello World' # This is a byte string. The 'b' before the string indicates that it is a byte string.
    f.write(data) # This will write the byte string in the file. The output will be in bytes format.

# Read
with open("bin.bin", "rb") as f: # rb : read binary mode
    data = f.read() # This will read the binary data from the file and store it in the variable 'data'
    print(data) # This will print the binary data in the console. The output will be in bytes format.
    print(type(data)) # This will print the type of data read from the file. It will be in bytes format because we are reading from a binary file.

# Write a list of data in a binary file
my_list = [1, 2, 3, 4, 5]
with open("bin.bin", "wb") as f: # wb : write binary mode
    for item in my_list:
        data = str(item).encode() # This will convert the integer into a byte string and then write it in the file.
        f.write(data) # This will write the byte string in the file. The output will be in bytes format.

# Read and write in a binary file
with open("bin.bin", "rb+") as f: # rb+ : read and write binary mode
    data = f.read() # This will read the binary data from the file and store it in the variable 'data'
    print(data) # This will print the binary data in the console. The output will be in bytes format.
    print(type(data)) # This will print the type of data read from the file. It will be in bytes format because we are reading from a binary file.
    f.write(b'Hello Python') # This will write the byte string in the file. The output will be in bytes format.

