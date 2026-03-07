class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lowarr = []
        midarr = []
        higharr = []
        
        for x in range(len(nums)):
            if nums[x] < pivot:
                lowarr.append(nums[x])
            elif nums[x] == pivot:
                midarr.append(nums[x])
            elif nums[x] > pivot:
                higharr.append(nums[x])
        return lowarr + midarr + higharr
