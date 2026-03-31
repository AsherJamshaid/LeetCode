class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prod = 1
        s = 0

        lst = [int(d) for d in str(n)]

        s+=sum(lst)
        for x in range(len(lst)):
            prod*=lst[x]
        if n % (prod + s) == 0:
            return True
        return False
