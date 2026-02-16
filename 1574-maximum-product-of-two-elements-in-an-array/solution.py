class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        result = (nums[0] - 1)  * (nums[1] - 1)
        return result
