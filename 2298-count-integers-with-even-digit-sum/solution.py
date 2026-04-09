class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        lst = []
        for x in range(2,num+1):
            lst = list(map(int, str(x)))
            if sum(lst) % 2 == 0:
                ans+=1
        return ans
