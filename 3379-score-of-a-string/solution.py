class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        for x in range(len(s)):
            if x == len(s) - 1:
                break
            else:
                score += abs(ord(s[x]) - ord(s[x+1]))
        return score
