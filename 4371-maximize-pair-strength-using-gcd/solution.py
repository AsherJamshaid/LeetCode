class Solution(object):
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        ans = -1
        for x in range(len(nums)):
            temp = 0
            for y in range(x+1,len(nums)):
                g = gcd(nums[x], nums[y])
                temp = (nums[x] * nums[y]) / (g * g)
                if temp > ans:
                    ans = temp
        return ans
