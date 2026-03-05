class Solution(object):
    def sumAndMultiply(self, n):
        s = str(n)
        
        x = ""
        for ch in s:
            if ch != '0':
                x += ch
        
        if x == "":
            return 0
        
        num = int(x)
        digit_sum = sum(int(d) for d in x)
        
        return num * digit_sum
        

