# Uppgift 5
ugly_list = ["is", "coming", "to", "town", 17]

def copy_list(x):
    beautiful_list = ["Santa", "Claus" ]
    for element in x:
        beautiful_list.append(element)
    return beautiful_list

print(copy_list(ugly_list))