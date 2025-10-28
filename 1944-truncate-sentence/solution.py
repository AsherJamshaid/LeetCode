class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        new = ""
        space = k
        count = 0
        for x in range(len(s)):
            if s[x] != " ":
                new = new + s[x]
            if s[x] == " ":
                count = count + 1
                if count == space:
                    break
                else:
                    new = new + s[x]
        return new


        
