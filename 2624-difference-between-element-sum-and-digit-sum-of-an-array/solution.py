class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0 
        sum2 = 0
        for x in range(len(nums)):
            sum1 = sum1 + nums[x]
            if nums[x] > 9:
                while nums[x] != 0:
                    temp = nums[x] % 10
                    sum2 = sum2 + temp
                    temp2 = nums[x] // 10
                    nums[x] = temp2

            else:
                sum2 = sum2 + nums[x]     
        return abs(sum1-sum2)  
