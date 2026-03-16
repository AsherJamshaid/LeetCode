class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)

        a = nums[0]
        b = nums[1]
        c = nums[len(nums)-1]
        d = nums[len(nums)-2]

        return (a*b) - (c*d)

