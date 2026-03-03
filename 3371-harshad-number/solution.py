class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp3 = x
        sum = 0
        while x != 0:
            temp2 = x % 10
            temp = x // 10
            x = temp
            sum+=temp2
        if temp3 % sum == 0:
            return sum
        else:
            return -1
