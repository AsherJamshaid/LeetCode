class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for x in range(len(s)-1):
            if abs(int(s[x]) - int(s[x+1])) > 2:
                return False
        return True
