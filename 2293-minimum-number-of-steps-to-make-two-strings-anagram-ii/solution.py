class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        hashing = [0] * 26
        hashing2 = [0] * 26
        ans = 0
        for x in range(len(s)):
            hashing[ord(s[x]) - ord("a")]+=1
        for x in range(len(t)):
            hashing2[ord(t[x]) - ord("a")]+=1
        
        for x in range(26):
            ans+=(abs(hashing[x]-hashing2[x]))
        return ans
