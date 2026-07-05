class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value = nums[len(nums)//2]
        if nums.count(value) == 1:
            return True
        return False
