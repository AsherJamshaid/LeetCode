class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashing = {}
        if len(set(nums)) == 1:
            return nums[0]
        for x in range(len(nums)):
            if nums[x] in hashing:
                hashing[nums[x]]+=1
            else:
                hashing[nums[x]] = 1
        freq_count = {}
        for val in hashing.values():
            if val in freq_count:
                freq_count[val] += 1
            else:
                freq_count[val] = 1

        for num in nums:
            if freq_count[hashing[num]] == 1:  
                return num

        return -1
