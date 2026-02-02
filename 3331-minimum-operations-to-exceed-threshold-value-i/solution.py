class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        for x in range(len(nums)):
            if nums[x] < k:
                count+=1
        return count
