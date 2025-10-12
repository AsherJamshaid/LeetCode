class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        new = ""
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                answer.append("FizzBuzz")
            elif x % 3 == 0 and x % 5 != 0:
                answer.append("Fizz")
            elif x % 5 == 0 and x % 3 != 0: 
                answer.append("Buzz")
            else:
                new = str(x)
                answer.append(new)
        return answer
        
