# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

def count_freq(s,char):
    count=0
    for c in s:
        if(c==char):
            count+=1
    return count

my_string = "hello how are you"
char = 'h'
print(count_freq(my_string,char))  # Output: 2