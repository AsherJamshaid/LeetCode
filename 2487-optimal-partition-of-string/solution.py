class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        temp = ""
        for x in range(len(s)):
            if s[x] not in temp:
                temp+=s[x]
            else:
                ans+=1
                temp=""
                temp+=s[x]
        return ans
