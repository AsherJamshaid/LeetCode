class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        s = 1  
        
        x = 2
        while x * x <= num:
            if num % x == 0:
                s += x
                if x != num // x:
                    s += num // x
            x += 1
        
        return s == num

