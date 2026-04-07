class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        idx = 0
        for x in range(len(num)-1,-1,-1):
            if num[x] != "0":
                break
            idx+=1
        return num[:len(num)-idx]
