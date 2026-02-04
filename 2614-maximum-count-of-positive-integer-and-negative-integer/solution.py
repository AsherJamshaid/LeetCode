class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negcount = 0
        poscount = 0

        for x in range(len(nums)):
            if nums[x] < 0:
                negcount+=1
            elif nums[x] > 0:
                poscount+=1
        return max(negcount,poscount)
