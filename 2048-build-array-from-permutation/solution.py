class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        for x in range(len(nums)):
            index = nums[x]
            ans[x] = nums[index]
        return ans
