class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        temp = ""
        res = ""
        for x in range(len(date)):
            if date[x] != "-":
                temp+=date[x]
            else:
                new = int(temp)
                temp2 = format(new,'b')
                res+=str(temp2)
                res+="-"
                temp=""
        if temp:
            res += format(int(temp), 'b')
        return res
