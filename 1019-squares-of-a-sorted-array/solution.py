class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in range(len(nums)):
            res.append(abs(nums[x] * nums[x]))
        
        return sorted(res)
