class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for x in range(len(nums)):
            arr = [int(d) for d in str(nums[x])]
            s = sum(arr)
            result.append(s)
        return min(result)
