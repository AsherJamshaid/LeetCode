class Solution(object):
    def maxSubarrayLength(self, nums, k):
        l = 0
        freq = {}
        maxlen = 0

        for r in range(len(nums)):
            if nums[r] in freq:
                freq[nums[r]] += 1
            else:
                freq[nums[r]] = 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen
