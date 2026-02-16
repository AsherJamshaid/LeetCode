class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    if (x*y) % k == 0:
                        count+=1
        return count
