class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        arr = [int(x) for x in n]
        return max(arr)
