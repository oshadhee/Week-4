import random

hidden = random.randint(1,20)

guess = int(input('Enter guess number between 1 to 20 : '))
while (guess != hidden):
    print(f'{guess} is not correnct')
    guess = int(input('Enter guess number between 1 to 20 : '))
print(f'{guess} was correct')