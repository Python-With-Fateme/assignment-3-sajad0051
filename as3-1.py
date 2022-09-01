import random
a=random.randint(1,30)
for i in range(6):
    t=(input('enter your guess(0-6)?'))
    if t==a:
        print('dorost')
        break
else:
    print('the end')
