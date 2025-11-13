def count_up_to(n):
    num = 1
    while num <= n:
        yield num   # gives one number at a time
        num += 1

# Using the generator
for number in count_up_to(5):
    print(number)