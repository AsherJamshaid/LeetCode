class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = list(map(int, str(abs(n))))
        return sum(temp)
