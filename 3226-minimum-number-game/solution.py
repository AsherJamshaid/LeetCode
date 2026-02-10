class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        nums.sort()
        for x in range(0,len(nums),2):
            if x  == len(nums) - 1:
                break
            else:
                arr.append(nums[x+1])
                arr.append(nums[x])
        return arr



