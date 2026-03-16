class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.lower()
        res = 0
        for x in range(len(temp)-1):
            if temp[x] != temp[x+1]:
                res+=1
        return res
