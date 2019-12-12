names = ["Caleb", "Sam", "Hazel", "Jennie" , "Lisa" , "Rose", "Jisoo"]

def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result

print(to_upper(names))