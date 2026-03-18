class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        x = num1.split('+')
        x[1] = x[1][:-1] 
        y = num2.split("+")
        y[1] = y[1][:-1] 
        
        a_real = int(x[0])
            
        a_img = int(x[1])
        
        b_real = int(y[0])
            
        b_img = int(y[1])
        return str(a_real * b_real - a_img * b_img) \
            + "+" + str(a_real * b_img + a_img * b_real) + "i";
