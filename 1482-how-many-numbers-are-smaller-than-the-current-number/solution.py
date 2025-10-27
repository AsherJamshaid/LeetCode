class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        test = 0
        result_array = []

        for x in range(len(nums)):
            count = 0
            test = nums[x]
            for y in range(len(nums)):
                if test > nums[y]:
                    count = count + 1
            result_array.append(count)
        return result_array
