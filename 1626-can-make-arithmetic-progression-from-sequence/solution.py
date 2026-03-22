class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) == 2:
            return True
        arr.sort()
        
        temp = arr[1] - arr[0]
        for x in range(len(arr)-1):
            if arr[x+1] - arr[x] != temp:
                return False
        return True
