class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashing = {}
        length = len(s)
        for x in range(len(s)):
            if s[x] in hashing:
                hashing[s[x]]+=1
            else:
                hashing[s[x]] = 1
        
        for x in hashing.values():
            if x == 2 or x == 1:
                continue
            elif x  % 2 == 0:
                length-=(x-2)
            else:
                length-=(x-1)
        return length
