# Problem: Create a guessing game where the user has 5 chances to guess a randomly generated number between 1 and 20. Provide feedback ("Too high!" or "Too low!") after each guess.
import random
print("Welcome to the guessing game!")
max_guess_chances=5
guess_num=0
guess_made_so_far=list()

secret_number=random.randint(1,20)

while guess_num<max_guess_chances:
    guess=int(input("Guess  a number between 1 and 20: "))
    if 1 <= guess <=20:
        guess_num+=1
        guess_made_so_far.append(guess)
        if guess == secret_number:
            print("Congratulations, you guessed the secret number!")
            break
        elif guess > secret_number:
            print("Too high, try again")
        else:
            print("Too low, Try again")
    else:
        print("Please enter the number between 1 to 20")
if guess_num==max_guess_chances and guess != secret_number:
    print(f"Sorry, you've run out of guesses. The secret number was {secret_number}")

print(f"Guesses you have made so far: {guess_made_so_far}")




