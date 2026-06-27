def part(nums , l , r):
    k = nums[r]
    start = l 
    for i in range(l , r+1):
        if nums[i]<=k:
            t = nums[i]
            nums[i] = nums[start]
            nums[start] = t
            start = start+1
    return start-1

def qksort(nums , l , r):
    if l>=r:
        return
    pv = part(nums, l , r)
    qksort(nums , l ,pv-1)
    qksort(nums , pv+1 , r)
    
def qk(nums):
    n = len(nums)
    qksort(nums , 0 , n-1)
    return nums

print(qk([48,113,23,50,70]))    
            