class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        new = str(n)
        if str(x) in new:
            if new[0] != str(x):
                return True
            return False
        return False
