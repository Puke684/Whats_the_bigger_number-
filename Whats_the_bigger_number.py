import time
from sys import exit

num_1 = 60.9
num_2 = 61

a = float(input(f'Which is the bigger number?\n>Is it {num_1} or {num_2}?\n>'))

if a.is_integer():
    a = int(a)

time.sleep(1)


print('ok fine')
b = input(f"are you sure it's {a}?\nType 'yes' or 'no'\n>")

if b.lower() == 'yes':
    print('ok lets see')
elif b.lower() == 'no':
    print("don't waste my time :/")
    exit()
else:
    print('its a YES or NO question...')
    exit()


time.sleep(1)


if a == max(num_1, num_2):
    print('good job yay!')
elif a == 67:
    print("like.. 6 7? hah")
elif a == 69:
    print('you are the funny?')    
elif a == (num_2):
    print("you're dumb what")
else:
    print(f'wtf, how did you get {a}')