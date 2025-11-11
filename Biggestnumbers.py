def find_max(numbers):
    max_num = numbers[0]   # assume first number is biggest
    for n in numbers:
        if n > max_num:    # if bigger number found
            max_num = n
    return max_num

# Example
list1 = [4, 12, 7, 25, 9]
print("Maximum number is:", find_max(list1))