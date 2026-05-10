class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = []
        for x in range(len(nums)):
            new.append(nums[x])
        nums.reverse()
        for x in range(len(nums)):
            new.append(nums[x])
        return new
