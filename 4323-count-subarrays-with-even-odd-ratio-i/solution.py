class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = 0
        for x in range(len(nums)):
            odd_count = 0
            even_count = 0     
            for y in range(x,len(nums)):
                if nums[y] % 2 != 0:
                    odd_count+=1
                else:
                    even_count+=1
                if odd_count > 0:
                    if even_count * b <= odd_count * a:
                        ans += 1
        return ans
