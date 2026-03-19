class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashing = {}
        res = []

        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]]+=1
            else:
                hashing[nums[x]] = 1
        for key,val in hashing.items():
            if val == 1:
                res.append(key)
            
        return res
