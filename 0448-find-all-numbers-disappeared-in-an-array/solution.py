class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        length = len(nums)
        result = []
        for x in range(1,length+1):
            if x not in s:
                result.append(x)
        return result
