class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        count = 0
        for x in range(size):
            for y in range(x+1,size):
                if abs(nums[x] - nums[y]) == k:
                    count+=1        
        return count

