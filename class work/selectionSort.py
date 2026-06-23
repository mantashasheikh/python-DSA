def myselection(nums):
    n = len(nums)
    for i in range(n):
        chotu = i
        for j in range(i+1, n):
            if nums[chotu] > nums[j]:
                chotu = j
        if chotu != i :
            t = nums[chotu]
            nums[chotu] = nums[i]
            nums[i] = t
    return nums

print(myselection([4,7,2,9,8,1]))                