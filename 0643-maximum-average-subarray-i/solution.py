class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0
        r = k - 1
        sum = 0
        avg = 0
        for x in range(l,r+1):
            sum+=nums[x]
        maxAvg = sum / float(k)
        while r < len(nums) - 1:
            sum-=(nums[l])
            l+=1
            r+=1
            sum+=nums[r]
            avg = sum / float(k)
            maxAvg = max(maxAvg,avg)
        return  maxAvg
