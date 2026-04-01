class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        ops = 0
        salary.sort()
        temp  = 0
        for x in range(len(salary)):
            if x == 0 or x == len(salary) - 1:
                continue
            temp+=salary[x]
            ops+=1
        return temp * 1.0 / ops
