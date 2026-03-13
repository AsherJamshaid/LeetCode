class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        sum = 0
        minlen = float('inf')

        while r < len(nums):
            sum+=nums[r]

            while sum >= target:
                minlen = min(minlen,r-l+1)
                sum-=nums[l]
                l+=1
                
            r+=1
        return 0 if minlen == float('inf') else minlen
