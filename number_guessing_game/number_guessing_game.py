import random

number = random.randint(1,300)
guess = None
attempts = 0 

print("I am thinking about a number between 1 and 300...")

while guess !=number: # ! means not equal too
    guess = int(input("Take a guess: "))
    attempts += 1 #increases the attempts counter by 1 each time the player makes a guess

    if guess < number: #checks if guess is smaller
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.") #checks if guess is louder

    else: #answer is correct so loop breaks
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
    