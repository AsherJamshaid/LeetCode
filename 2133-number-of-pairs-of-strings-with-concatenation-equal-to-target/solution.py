class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        count = 0
        for x in range(len(nums)):

            for y in range(len(nums)):
                if x == y:
                    continue
                elif nums[x] + nums[y] == target:
                    count+=1
        return count
