class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = False   

        for x in range(len(nums)):
            if nums[x] % 2 == 0 and nums.count(nums[x]) == 1:
                flag = True
                val = nums[x]
                break
        if flag:
            return val
        else:
            return -1
