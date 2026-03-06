class Solution(object):
    def subarraySum(self, nums):
        ans = 0
        
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            
            for j in range(start, i+1):
                ans += nums[j]
                
        return ans
