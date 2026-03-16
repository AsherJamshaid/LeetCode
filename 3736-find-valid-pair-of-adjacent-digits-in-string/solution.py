class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        flag = False
        temp = ""
        for x in range(len(s)-1):
            if s[x] != s[x+1]:
                if s.count(s[x]) == int(s[x]) and s.count(s[x+1]) == int(s[x+1]):
                    flag = True
                    temp = s[x] + s[x+1]
                    break
        if flag:
            return temp
        return ""
