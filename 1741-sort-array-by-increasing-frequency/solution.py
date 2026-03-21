class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}

        for x in range(len(nums)):
            if nums[x] in freq:
                freq[nums[x]] += 1
            else:
                freq[nums[x]] = 1
        
        result = sorted(nums, key=lambda x: (freq[x], -x))

        return result
