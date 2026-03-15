class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashing = {}
        res = 0
        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]]+=1
            else:
                hashing[nums[x]] = 1
        max_freq = max(hashing.values())
        for freq in hashing.values():
            if freq == max_freq:
                res+=freq
        return res
        
