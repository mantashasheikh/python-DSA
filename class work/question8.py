# remove duplicate from sorted array II (80)
class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n<=2:
            return n
        s = 1     
        for i in range(2,n):
            if nums[i] != nums[s-1]:
               s = s+1
               nums[s] = nums[i]
        return s+1 