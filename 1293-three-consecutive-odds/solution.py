class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flag = False
        count = 0
        for x in range(len(arr)):
            if arr[x] % 2 != 0:
                count+=1
            else:
                count = 0
            if count == 3:
                flag = True
        if flag:
            return True
        else:
            return False
