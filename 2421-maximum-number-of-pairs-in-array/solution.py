class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans1 = 0
        ans2 = 0 
        res = []

        freq = {}
        for x in range(len(nums)):
            if nums[x] in freq:
                freq[nums[x]] +=1 
            else:
                freq[nums[x]] = 1
            
        for key in freq.values():
            if key % 2 == 0:
                ans1+=(key//2)
            else:
                ans1+=(key//2)
                ans2+=1
        res.append(ans1)
        res.append(ans2)
        return res
