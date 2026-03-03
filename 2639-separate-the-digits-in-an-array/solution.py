class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        strin = ""
        new = []
        for x in range(len(nums)):
            strin+=str(nums[x])
        new = list(strin)
        new2 = list(map(int,new))
        return new2

