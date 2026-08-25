class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        temp = 0
        for x in range(n-1):
            result.append(x+1)
            temp+=(x+1)
        result.append(-temp)
        return result
