class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = len(set(nums))
        if 0 in nums:
            return new - 1
        return new
