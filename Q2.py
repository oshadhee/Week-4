total = 0 
count = 0 

score = int(input('Enter your scores, (Enter -9 to end) : '))

if score == -9 and count == 0:
    print('enter at least one score')
else:
    while(score != -9):
        total += score
        count += 1
        score = int(input('Enter your next score : '))
    average = float(total)/count
    print('Class average is', average)