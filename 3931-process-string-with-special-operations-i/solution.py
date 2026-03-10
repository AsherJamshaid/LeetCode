class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for x in range(len(s)):
            if s[x].islower():
                res.append(s[x])
            elif s[x] == "*":
                if len(res) != 0:
                    res.pop()
            elif s[x] == "#":
                for y in range(len(res)):
                    res.append(res[y])
            else:
                res.reverse()
        return ''.join(res)
            
