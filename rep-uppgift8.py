# Uppgift 8
# cities = ["Stockholm", "New York", "Tokyo", "Berlin"]

# def contains(a,b):
#     if b in a:
#         return True
#     if not b in a:
#         return False 

# print(contains(cities, "New York"))

cities = ["Stockholm", "New York", "Tokyo", "Berlin"]

def contains(a,b):
    for element in a:
        if b in a:
            return True
        else:
            return False

print(contains(cities, "Stockholm"))