def avg(*nums):
    sum = 0
    for i in nums:
        sum += i
    print("Avg is:",sum/len(nums))
avg(2,4,6)        