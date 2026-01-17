class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        large_sum = 0
        smallest_sum = 0
        nums.sort(reverse=True)
        for x in range(k):
            large_sum+=nums[x]
        nums.sort()
        for x in range(k):
            smallest_sum+=nums[x]
        return abs(large_sum - smallest_sum)
