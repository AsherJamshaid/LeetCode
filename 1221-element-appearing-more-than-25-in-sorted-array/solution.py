class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}

        for x in range(len(arr)):
            if arr[x] in freq:
                freq[arr[x]] += 1
            else:
                freq[arr[x]] = 1
            
        for val,key in freq.items():
            if key > len(arr) // 4:
                return val
        
