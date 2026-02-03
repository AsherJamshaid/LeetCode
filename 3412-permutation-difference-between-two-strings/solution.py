class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sum = 0

        for x in range(len(s)):
            for y in range(len(s)):
                if s[x] == t[y]:
                    sum+=abs(x-y)
        return sum
