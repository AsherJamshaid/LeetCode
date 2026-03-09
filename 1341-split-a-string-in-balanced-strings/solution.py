class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        bal_l = 0
        for x in range(len(s)):
            if s[x] == "L":
                bal_l+=1
            else:
                bal_l-=1
            if bal_l == 0:
                ans+=1
        return ans
