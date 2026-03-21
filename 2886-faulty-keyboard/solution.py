class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = ""
        temp = ""
        for x in range(len(s)):
            if s[x] == "i":
                temp = new[::-1]
                new = temp
            else:
                new+=s[x]
        return new
