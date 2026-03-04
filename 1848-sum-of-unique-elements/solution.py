class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        new = set(nums)
        new2 = list(new)
        for x in range(len(new)):
            if nums.count(new2[x])== 1:
                ans+=new2[x]
        return ans
