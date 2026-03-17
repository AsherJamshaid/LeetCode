class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        even_min = float('inf')
        odd_max = 0

        new = set(s)
        new2 = list(new)
        for x in range(len(new)):
            temp = s.count(new2[x])
            if temp % 2 == 0:
                even_min = min(even_min,temp)
            else:
                odd_max = max(odd_max,temp)
        return odd_max - even_min
