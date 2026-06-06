# remove duplicate from sorted array (26)
class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        s = 0
        for i in range(1,n):
           if  nums[i] != nums[s]:
               s = s + 1
               nums[s] = nums[i]
        return s+1  

     