class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        flag = False
        for x in range(len(num)):
            if int(num[x]) % 2 != 0:
                flag = True
                break
        if flag == False:
            return ""
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]

        return ""
