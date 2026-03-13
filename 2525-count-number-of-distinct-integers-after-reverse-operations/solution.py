class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)):
            temp = str(nums[x])
            temp2 = temp[::-1]
            nums.append(int(temp2))
        return len(set(nums))
