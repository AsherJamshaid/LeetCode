class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ans = 100
        flag = False
        for x in range(len(nums)):

            for y in range(len(nums)):
                if x == y:
                    continue
                elif nums[x] == 1 and nums[y] == 2:
                    temp = abs(y-x)
                    min_ans = min(min_ans,temp)
                    flag = True
        if flag:
            return min_ans
        return -1

