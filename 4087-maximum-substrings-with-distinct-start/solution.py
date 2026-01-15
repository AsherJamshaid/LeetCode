class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for x in range(len(s)):
            temp = s[x+1::]
            if s[x] not in temp:
                count+=1
        return count
