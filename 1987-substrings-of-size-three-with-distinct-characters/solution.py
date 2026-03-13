class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        k = 3
        l = 0
        r = k - 1
        temp = ""
        if len(s) < 3:
            return 0
        for x in range(l,r+1):
            temp+=s[x]
        if len(temp) == len(set(temp)):
            ans+=1
        
        while r < len(s) - 1:
            temp = temp[1:]
            l+=1
            r+=1
            temp+=s[r]
            if len(temp) == len(set(temp)):
                ans+=1
        return ans
