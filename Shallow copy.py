import copy

original = [1, 2, [3, 4]]
shallow = copy.copy(original)

print("Original:", original)    # [1, 2, [3, 4]]
print("Shallow :", shallow)     # [1, 2, [3, 4]]

# Change nested list
shallow[2][0] = 99

print("After modification:")
print("Original:", original)    # [1, 2, [99, 4]]  (changed!)
print("Shallow :", shallow) 