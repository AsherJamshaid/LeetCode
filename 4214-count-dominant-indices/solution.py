class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for x in range(len(nums)-1):
            avg = 0
            sum = 0
            for y in range(x+1,len(nums)):
                sum+=nums[y]
            avg = sum / (len(nums) - (x+1))
            if nums[x] > avg:
                count+=1
        return count
