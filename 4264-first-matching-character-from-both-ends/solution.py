class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        for x in range(len(s)):
            if s[x] == s[len(s) - x - 1]:
                return x
        return -1
