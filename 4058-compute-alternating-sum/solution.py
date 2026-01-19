class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add = 0
        minus = 0
        for x in range(len(nums)):
            if x % 2 == 0:
                add+=nums[x]
            else:
                minus+=nums[x]
        return add - minus
