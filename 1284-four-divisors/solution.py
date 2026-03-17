import math
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum2 = 0
        for x in range(len(nums)):
            count = 0
            arr=[]
            for y in range(1,int(math.sqrt(nums[x])+1)):
                if nums[x] % y== 0:
                    arr.append(y)
                    if y != nums[x] // y:
                        arr.append(nums[x] // y)
                    if len(arr) > 4:  
                        break
            if len(arr) == 4:  
                sum2 += sum(arr)
        return sum2

