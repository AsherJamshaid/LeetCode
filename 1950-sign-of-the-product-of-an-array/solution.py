class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = 1
        for x in range(len(nums)):
            prod*=nums[x]
        if prod < 0:
            return -1
        elif prod > 0:
            return 1
        return 0
