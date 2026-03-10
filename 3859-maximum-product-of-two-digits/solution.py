class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = list(map(int,str(n)))
        arr.sort(reverse=True)
        return arr[0] * arr[1]
