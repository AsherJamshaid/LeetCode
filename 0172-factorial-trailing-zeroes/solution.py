class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n/3125+n/625+n/125+n/25+n/5
