class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        num1 = []
        num2 =[]
        result = []
        for x in range(n):
            num1.append(nums[x])
        for x in range(n,2*n):
            num2.append(nums[x])

        for x in range(n):
            result.append(num1[x])
            result.append(num2[x])
        return result
