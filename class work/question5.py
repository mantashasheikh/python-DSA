#Running sum (1480)
class Solution(object):
    def runningSum(self, nums):
        r = []
        r.append(nums[0])
        for i in range(1,len(nums)):
            a = r[i-1] + nums[i]
            r.append(a)
        return r       

