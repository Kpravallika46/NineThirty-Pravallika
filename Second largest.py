def second_largest(numbers):
    numbers = list(set(numbers))  
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[-2]
numbers = [10, 20, 4, 45, 99]
print("Second largest element is:", second_largest(numbers))