class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for x in range(len(nums)):
            temp = []

            for y in range(x,len(nums)):
                temp.append(nums[y])
                ans+=(len(set(temp))) * (len(set(temp)))
        return ans
