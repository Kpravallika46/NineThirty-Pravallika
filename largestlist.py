#Largest number from list
nums=[42,51,62,36,47]
large=nums[0]
for num in nums:
    if num > large:
        large=num
        print(large)
