class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        temp = 0
        temp2 = 0
        for x in range(k):
            temp2 = min(nums)
            temp = nums.index(temp2)
            nums[temp] = temp2 * multiplier
        return nums
