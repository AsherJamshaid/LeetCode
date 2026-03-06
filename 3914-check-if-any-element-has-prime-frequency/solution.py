from math import sqrt
class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = False
        temp = set(nums)
        temp3 = list(temp)
        temp2 = 0
        for x in range(len(temp)):
            temp2 = nums.count(temp3[x])
            if temp2 <= 1:
                    continue
            another = False
            for y in range(2,int(sqrt(temp2))+1):
                if temp2 % y == 0:
                    another = True
                    break
            if another == False:
                flag = True
                break
        if flag:
            return True
        else:
            return False
