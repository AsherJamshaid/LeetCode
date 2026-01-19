class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [] * 2

        for x in range(len(nums)):
            found = False
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    result.append(nums[x])
                    break
        return result
