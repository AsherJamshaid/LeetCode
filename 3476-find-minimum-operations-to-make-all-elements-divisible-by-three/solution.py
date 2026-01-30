class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for x in range(len(nums)):
            rem = nums[x] % 3
            if rem == 1:
                count+=1
            elif rem == 2:
                count+=1
        return count
