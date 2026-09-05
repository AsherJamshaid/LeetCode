class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        res = 0
        cursum = 0
        prefixsum = { 0:1 }
        for n in nums:
            cursum+=n
            diff = cursum - goal
            res+=prefixsum.get(diff,0)
            prefixsum[cursum] = 1 + prefixsum.get(cursum,0)
        return res
