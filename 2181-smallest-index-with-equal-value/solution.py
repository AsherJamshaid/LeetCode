class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)):
            if x % 10 == nums[x]:
                return x
        return -1
