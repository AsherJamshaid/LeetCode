class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        result = []
        value = 0
        for x in range(len(nums)//2):
            nums.sort(reverse=True)
            maxvalue = nums[0]
            minvalue = nums[len(nums)-1]
            value = (minvalue + maxvalue) / 2.0
            result.append(value)
            nums.pop(0)
            nums.pop(len(nums)-1)
        return min(result)

