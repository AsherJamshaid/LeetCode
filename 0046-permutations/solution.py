class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []

        def generate(current, remaining):
            if len(remaining) == 0:
                result.append(current)
                return
            for i in range(len(remaining)):
                num = remaining[i]
                generate(current + [num], remaining[:i] + remaining[i+1:])
        generate([], nums)
        return result
