hidden = 6
guess = int(input('Enter a guess number between 1 to 20 : '))
while (guess != hidden):
    print(f'{guess} is not correct')
    guess = int(input('Enter a guess number between 1 to 20 : '))
print(f'{guess} was correct')