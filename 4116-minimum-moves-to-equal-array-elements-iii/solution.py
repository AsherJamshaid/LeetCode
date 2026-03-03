class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        first = max(nums)
        for x in range(len(nums)):
            count+=first - nums[x]
        return count
