class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        first = nums[0]
        last = nums[len(nums) - 1]
        result = []
        for x in range(first,last+1):
            if x not in nums:
                result.append(x)
        result.sort()
        return result
