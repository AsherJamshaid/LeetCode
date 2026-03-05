class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        temp = 0
        temp = max(nums)
        for x in range(k):
            ans+=temp
            temp+=1
        return ans
