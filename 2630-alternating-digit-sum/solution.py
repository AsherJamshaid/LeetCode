class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        digits = list(map(int, str(n)))
        for x in range(len(digits)):
            if x % 2 == 0:
                res+=digits[x]
            else:
                res-=digits[x]
        return res
