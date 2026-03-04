class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        first = nums[0]
        sec = nums[1]
        third = nums[len(nums)-1]
        return ((first+sec) - third)
