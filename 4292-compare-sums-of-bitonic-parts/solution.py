class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ascarr = 0
        descarr = 0
        peak_index = 0
        for x in range(1,len(nums)):
            if nums[x] > nums[x-1]:
                peak_index = x
        ascarr = sum(nums[:peak_index+1])
        descarr = sum(nums[peak_index:])
        if ascarr > descarr:
            return 0
        elif ascarr < descarr:
            return 1
        else:
            return -1
