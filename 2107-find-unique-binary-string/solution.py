class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        nums_set = set(nums)
        
        for i in range(2**n):
            bin_str = bin(i)[2:] 
            bin_str = bin_str.zfill(n)
            if bin_str not in nums_set:
                return bin_str

