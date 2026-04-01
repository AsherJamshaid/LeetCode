class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        res = []
        for x in range(len(nums)):

            for y in range(x,len(nums)):
                if abs(x-y) >= indexDifference and abs(nums[x]-nums[y]) >= valueDifference:
                    res.append(x)
                    res.append(y)
                    return res
        new = []
        new.append(-1)
        new.append(-1)
        return new
