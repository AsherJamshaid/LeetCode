class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """

        new = str(n)
        new2 = new[::-1]
        return(abs(n-int(new2)))
