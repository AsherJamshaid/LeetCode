class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_n,max_cnt = max(nums), 0
        l = 0
        res = 0
        r = 0
        while r < len(nums):
            if nums[r] == max_n:
                max_cnt+=1
            
            while max_cnt > k or(l <= r and max_cnt == k and nums[l] != max_n):
                if nums[l] == max_n:
                    max_cnt-=1
                l+=1
            if max_cnt == k:
                res+= l+ 1
            r+=1
        return res
