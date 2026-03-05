class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new = set(nums)
        new2 = list(new)
        temp = 0
        result = 0
        for x in range(len(new)):
            temp = nums.count(new2[x])
            if temp % k == 0:
                result = result + (temp * new2[x])
        return result
