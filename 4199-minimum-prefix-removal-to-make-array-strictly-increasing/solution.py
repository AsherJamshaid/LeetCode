class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        ops = 0
        for x in range(len(nums)-1,-1,-1):
            if nums[x] <= nums[x-1]:
                ops = x
                break
        return ops
