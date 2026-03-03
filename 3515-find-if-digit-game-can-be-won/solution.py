class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = 0
        sum2 = 0

        for x in range(len(nums)):
            if nums[x] // 10 == 0:
                sum1+=nums[x]
            else:
                sum2+=nums[x]
        return sum1 != sum2
