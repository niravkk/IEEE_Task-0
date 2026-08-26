def process_list(numbers):
    nums = numbers.copy()
    numPos = []
    for i in range(len(nums)):
        if nums[i] >0:
            numPos.append(nums[i])
    nums.sort()
    return numPos
original = [5, -2, 8, -1, 3]
result = process_list(original)
print("Original:", original)
print("Result:", result)