class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ans = float('inf')
        for x in range(len(nums)):
            if nums[x] == target:
                temp = abs(x-start)
                ans = min(ans,temp)
        return ans
