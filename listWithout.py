def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):  
        reversed_list.append(lst[i])
    return reversed_list
numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
print("Reversed List:", reverse_list(numbers))