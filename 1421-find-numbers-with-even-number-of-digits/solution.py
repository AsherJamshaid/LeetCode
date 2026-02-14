class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for x in range(len(nums)):
            num = nums[x]
            length = len(str(num))
            if length % 2 == 0:
                count+=1
        return count
