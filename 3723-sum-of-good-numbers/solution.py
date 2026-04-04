class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for x in range(len(nums)):
            if ((x-k) < 0 or nums[x] > nums[x-k]) and ((x+k) >= len(nums) or nums[x] > nums[x+k]):
                res+=nums[x]
        return res
