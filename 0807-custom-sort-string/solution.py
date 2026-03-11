class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        hashing = {}
        new = ""
        for x in range(len(s)):
            if s[x] in hashing:
                hashing[s[x]]+=1
            else:
                hashing[s[x]] = 1
        for x in range(len(order)):
            if order[x] in hashing:
                new+=order[x] * hashing[order[x]]
                del hashing[order[x]]
        for x in hashing:
            new+=x * hashing[x]
        return new

