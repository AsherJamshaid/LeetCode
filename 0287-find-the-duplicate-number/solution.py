class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashing = {}

        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]] += 1
            else:
                hashing[nums[x]] = 1

        for freq,val in hashing.items():
            if val >= 2:
                return freq
