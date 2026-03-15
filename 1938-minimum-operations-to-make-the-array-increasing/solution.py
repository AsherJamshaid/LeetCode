class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        res = 0
        for x in range(len(nums)-1):
            if nums[x] >= nums[x+1]:
                temp = (nums[x]-nums[x+1]) + 1
                res+=temp
                nums[x+1] = temp + nums[x+1]
        return res
