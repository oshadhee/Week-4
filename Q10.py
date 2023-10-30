import random

hidden_number = random.randint(1, 20)

attempts = 0  
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the number between 1 and 20: "))
    
    if guess == hidden_number:
        print(f"Congratulations! You guessed the number {hidden_number} in {attempts + 1} attempts.")
        break
    elif guess < hidden_number:
        print("The correct number is higher.")
    else:
        print("The correct number is lower.")
    
    attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The hidden number was {hidden_number}.")