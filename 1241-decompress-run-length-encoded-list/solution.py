class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x in range(0,len(nums)-1,2):
            count = nums[x]
            for y in range(count):
                result.append(nums[x+1])
        return result
