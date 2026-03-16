class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        ans = -1
        
        while l < r:
            s = nums[l] + nums[r]
            
            if s == 0:
                ans = max(ans, nums[r])
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
        
        return ans
