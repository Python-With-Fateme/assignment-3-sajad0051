import random
a=random.randint(1,30)
for i in range(6):
    t=int(input('enter your guess(0-6)?'))
    if t==a:
        print('dorost')
        break
    if t>a :
        print('bala hast')
    else:
        print('pain hast')
