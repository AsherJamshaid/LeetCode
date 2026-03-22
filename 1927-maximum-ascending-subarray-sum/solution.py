class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = 0
        for x in range(len(nums)):
            temp = nums[x]
            ptr = x
            for y in range(x+1,len(nums)):
                if nums[ptr] < nums[y]:
                    temp+=nums[y]
                    ptr+=1
                else:
                    break
            if temp > maxsum:
                maxsum = temp
        return maxsum
