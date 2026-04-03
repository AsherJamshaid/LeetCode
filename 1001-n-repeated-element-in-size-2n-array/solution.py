class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        hashing = {}

        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]]+=1
            else:
                hashing[nums[x]] = 1
        
        for key,val in hashing.items():
            if val == n:
                return key
