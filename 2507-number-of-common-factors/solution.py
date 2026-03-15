class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = 1

        for x in range(2,b+1):
            if a % x == 0 and b % x == 0:
                ans+=1
        return ans
