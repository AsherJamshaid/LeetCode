class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = max(nums)
        ind = nums.index(temp)
        flag = False
        for x in range(len(nums)):
            if ind == x:
                continue
            
            elif temp < (2*nums[x]):
                flag = True
                break
            
        if flag:
            return -1
        else:
            return ind
