n= int(input())
print()
nums =[]
for i in range(n):
    temp = int(input())
    nums.append(temp)

max = nums[0]
min = nums[0]
sumEven =0
sumOdd =0
numsRev = nums[::-1]
for i in nums:
    if i > max:
        max = i
    if i<min:
        min =i
    if i%2==0:
        sumEven+=i
    else:
        sumOdd+=i
sum = sumEven+sumOdd
print("Largest: ", max)
print("Smallest: ", min)
print("Sum: ", sum)
print("Sum of even: ", sumEven)
print("Sum of odd: ", sumOdd)
print("Reversed: ", end ="")
for j in numsRev:
    print(j, end=" ")