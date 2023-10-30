import random

hidden = random.randint(1,20)

guess = int(input('Enter guess number between 1 to 20 : '))
while (guess != hidden):
    print(f'{guess} is not correnct')
    if guess > hidden:
        print('guess is too high')
    else:
        print('guess is too low')
    guess = int(input('Enter guess number between 1 to 20 : '))
print(f'{guess} was correct')