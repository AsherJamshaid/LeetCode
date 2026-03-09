class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = False
        for x in range(len(nums)):
            temp = list(map(int, str(nums[x])))
            if sum(temp) == x:
                return x
        return -1
