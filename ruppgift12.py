import random

def divisble_by(number):
    for i in range(1,1000):
        if number % 7 == 0:
            return True
        else:
            return False

print(divisble_by(random.randrange(1,1000)))