def is_even(a):
    if a % 2 == 0:
        return True
    if a % 2 > 0:
        return False

numbers = [1,3,2,89,106]

def evens(numbers):
    res = []
    for b in numbers:
       if b % 2 == 0:
           res.append(b)
    return res

print(evens(numbers))