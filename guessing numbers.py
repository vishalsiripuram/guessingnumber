import random
b=random.randint(1,10)
guess=True
guesses=0
print(b)
while guess:
    a = int(input("Guess the number between 1-10"))
    if a==b:
        guesses+=1
        print("hey you won and no of guesses {}".format(guesses))
        guess=False
    elif a>b:
        guesses+=1
        print("hey you entered greter value than expected")
    else:
        guesses+=1
        print("you entered lower than the expected")
if guesses==10:
    print("No.of guesses exceeded")