class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        temp2 = -1
        for x in range(len(nums)):
            temp = int(max(str(nums[x]))) - int(min(str(nums[x])))
            if temp > temp2:
                temp2 = temp
        for x in range(len(nums)):
                if (int(max(str(nums[x]))) - int(min(str(nums[x])))) == temp2:
                    total+=nums[x]
        return total
