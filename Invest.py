def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
print("Inverted Dictionary:", invert_dict(my_dict))