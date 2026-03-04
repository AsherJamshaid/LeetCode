class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for x in range(1,len(nums)+1):
            if len(nums) % x == 0:
                total+=(nums[x-1] * nums[x-1])
        return total
