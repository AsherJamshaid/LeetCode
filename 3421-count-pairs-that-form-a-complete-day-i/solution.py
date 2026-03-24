class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        res = 0
        for x in range(len(hours)):

            for y in range(x+1,len(hours)):
                if (hours[x] + hours[y]) % 24 == 0:
                    res+=1
        return res
