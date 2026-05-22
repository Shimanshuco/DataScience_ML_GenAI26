import random

val = random.randint(1, 100)
num = int(input("Enter a guess"));
attempts = 0;
while True:
    if(val==num):

        print("Your guess was right");
        break;
    elif(num>val):
        print("Value is greater. Guess small !")
        attempts=attempts+1
    else : 
        print("Value is smaller. Guess large !")
        attempts=attempts+1
    num = int(input("Enter a guess"));

print("Total Attempts ",attempts);