import random 

x = random.randint(1,101)

guess = int (input("Enter the guess: "))

score = 0

while guess != x:
    if guess > x:
        guess = int(input(f"Enter lower number: "))
        
    elif guess < x:
        guess = int(input(f"Enter higher number: "))
        
    score +=1

print(f"You took {score+1} try to guess the number")
