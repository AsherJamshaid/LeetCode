class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = 0
        if "a" not in s and "e" not in s and "i" not in s and "o" not in s and "u" not in s:
            return False
        else:
            for x in range(len(s)):
                if s[x] == "a" or s[x] == "e" or s[x] == "i" or s[x] == "o" or s[x] == "u":
                    temp+=1
            if temp % 2 != 0:
                return True
        return True
