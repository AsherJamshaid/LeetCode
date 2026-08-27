class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 1
        new = s[0]

        for x in range(1, len(s)):

            if s[x] == s[x-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                new += s[x]

        return new

      
