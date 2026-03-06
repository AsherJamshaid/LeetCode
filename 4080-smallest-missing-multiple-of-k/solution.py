class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        a = 1
        temp = 0
        val = 0
        while True:
            temp = a*k
            if (temp % k == 0) and (temp not in nums):
                val = temp
                break
            a+=1
        return val
