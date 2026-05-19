print("Hello World")
#Python is a case sensitive language.
print("My name is Himanshu Singh");

#print(Himanshu Singh) 
#This will give an error because we have not defined the variable Himanshu Singh. 
# We need to put it in quotes to make it a string.

print(4)

print(True)

print("Hello", "World", "Welcome to Python",1,True,4.5);
# In the above line we are printing multiple values of different data types.

#print() Syntax : 
# print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# value1, value2, ... : These are the values to be printed.
    # They can be of any data type (string, integer, float, boolean, etc.) and can be separated by commas.
# sep : This is an optional parameter that specifies the separator between the values.
    # By default, it is a space (' '), but you can change it to any string (e.g., comma, hyphen, etc.).
# end : This is an optional parameter that specifies what to print at the end of the output.
    #  By default, it is a newline character ('\n'), which means that the next print 
    # statement will start on a new line. You can change it to any string (e.g., space, tab, etc.) 
    # or even an empty string ('') if you don't want any separation.

print("Hello", "World", sep="-");

print("Hello")
print("World")
# The above two print statements will print "Hello" and "World" on separate lines 
    #  because the default end parameter is a newline character.

print("Hello", end=" ");
print("World");
# The above two print statements will print "Hello" and "World" on the same line 
    # because we have changed the end parameter to a space.