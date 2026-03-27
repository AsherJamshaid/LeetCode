class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        i = n
        lst = []
        while True:
            temp = 1
            lst = list(map(int, str(i)))
            for x in range(len(lst)):
                temp*=lst[x]
            if temp % t == 0:
                return i
            else:
                i+=1

