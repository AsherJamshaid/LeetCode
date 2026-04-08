class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = abs(nums[0]-nums[len(nums)-1])
        for x in range(len(nums)-1):
            temp = abs(nums[x]-nums[x+1])
            if temp > max_diff:
                max_diff = temp
        return max_diff
