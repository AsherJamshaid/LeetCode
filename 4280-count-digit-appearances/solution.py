class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        ans = 0

        for x in range(len(nums)):
            temp = list(map(int, str(nums[x])))
            for y in range(len(temp)):
                if temp[y] == digit:
                    ans+=1
        return ans
