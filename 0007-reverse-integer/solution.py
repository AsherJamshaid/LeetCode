class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0 
        if x > 0:
            while x > 0:
                last_digit = x % 10
                x = x / 10
                res = (res * 10) + last_digit
            if res<-2147483648 or res>2147483647:
                return 0
            return res
        elif x < 0:
            while abs(x) > 0:
                last_digit = abs(x) % 10
                x = abs(x) / 10
                res = (res * 10) + last_digit
            if res<-2147483648 or res>2147483647:
                return 0
            return -(res)
        return 0
       
