class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_dist = float('inf')
        found = False

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] == nums[j] == nums[k]:
                        found = True
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        min_dist = min(min_dist,dist)
        if found:
            return min_dist
        return -1
