class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("A") >= 2:
            return False
        temp = 0
        flag = False
        for x in range(len(s)):
            if s[x] == "L":
                temp+=1
            else:
                temp = 0
            if temp >= 3:
                flag = True
                break
        if flag:
            return False
        return True
