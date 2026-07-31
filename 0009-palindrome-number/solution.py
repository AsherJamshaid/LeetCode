class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        temp = x
        while x > 0:
                last_digit = x % 10
                x = x / 10
                res = (res * 10) + last_digit
        if res == temp:
            return True
        return False
