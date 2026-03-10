class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new = set(nums)
        new2 = list(new)
        new2.sort(reverse=True)
        res = []
        if k > len(new2):
            for x in range(len(new2)):
                res.append(new2[x])
        else:
            for x in range(k):
                res.append(new2[x])
        return res
