import random

num_rolls = 100
num_doubles = 0

for _ in range(num_rolls):
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  

    if die1 == die2:  
        num_doubles += 1

print(f'Out of {num_rolls} rolls, you rolled {num_doubles} doubles.')
