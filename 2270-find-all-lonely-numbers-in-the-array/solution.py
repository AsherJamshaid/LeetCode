class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        hashing = {}

        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]]+=1
            else:
                hashing[nums[x]]=1

        for freq,val in hashing.items():
            if val == 1:
                if freq + 1 not in hashing and freq - 1 not in hashing:
                    res.append(freq)
        return res
