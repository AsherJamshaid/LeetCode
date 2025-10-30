class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        size = len(nums)
        found = False
        for x in range(size):
            for y in range(1,size):
                if x == y:
                    continue
                elif nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    found  = True
                    break
            if found == True:
                break
        return result
