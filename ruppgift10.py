import random

def randomlist(number):
    mylist = []
    for i in range(number):
        mylist.append(random.randrange(0,100))
    return mylist

print(randomlist(5))    