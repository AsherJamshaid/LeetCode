class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        add = 0

        for x in range(len(nums)):
            add = add + nums[x]
            result.append(add)
        return result

