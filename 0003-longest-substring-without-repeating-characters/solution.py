class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        l = 0 
        r= 0 
        hashing = [-1] * 256

        while r < len(s):
            if hashing[ord(s[r])] != -1:
                if hashing[ord(s[r])] >= l:
                    l = hashing[ord(s[r])] + 1
            length = r - l + 1
            maxlen = max(maxlen,length)
            hashing[ord(s[r])] = r
            r+=1
        return maxlen
