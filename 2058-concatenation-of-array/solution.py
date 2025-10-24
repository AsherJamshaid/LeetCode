class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in range(len(nums)):
            ans.append(nums[x])
        for y in range(len(nums)):
            ans.append(nums[y])
        return ans
