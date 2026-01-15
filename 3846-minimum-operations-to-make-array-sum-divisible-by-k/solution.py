class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        while True:
            found = False
            for x in range(len(nums)):
                if sum(nums) % k == 0:
                    found = True
                    break
                else:
                    count+=1
                    nums[x] = nums[x] - 1
            if found == True:
                break
        return count
