class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        position = 0

        for x in range(len(nums)):
            position = index[x]
            target.insert(position, nums[x])
        return target
