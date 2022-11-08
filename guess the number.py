# Little advanced Guess Game
import random
print("Hello! What is your name?")
name = input()
print("Well, " + name + ", I am thinking of a number between 1 and 10")
number = random.randint(1, 10)
guess_taken = 0
guess = ()
# using loop to take the guess
while guess_taken < 3:
    print("Take a Guess : ")
    guess = input()
    guess = int(guess)
    guess_taken += 1
    if guess < number:
        print("Your guess is  low.")
    elif guess > number:
        print("Your guess is  high.")
    else:
        print("Your guess is  correct.")
        break

if guess == number:
    print(f'Good job, { name }! You guessed my number in {guess_taken} guesses!')

if guess != number:
    print(f"Nope. The number I was thinking of was {number}")
