class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        let = "zyxwvutsrqponmlkjihgfedcba"
        ans = 0
        for x in range(len(s)):
            for y in range(len(let)):
                if s[x] == let[y]:
                    prod = (x+1) * (y+1)
                    ans+=prod
        return ans
