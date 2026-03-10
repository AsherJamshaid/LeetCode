class Solution(object):
    def findDuplicates(self, nums):
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
                hashing[nums[x]] = 1
        ans = 0
        for num,f in hashing.items():
            if f == 2:
                ans = num
                res.append(ans)
        return res
