class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers can never be palindrome
        if x < 0:
            return False

        # Convert integer to string
        s = str(x)

        # Reverse the string using slicing
        rev = s[::-1]

        # Compare original and reversed
        return s == rev

