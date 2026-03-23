class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0 
        for x in range(len(arr1)):
            flag = False
            for y in range(len(arr2)):
                if abs(arr1[x] - arr2[y]) <= d:
                    flag = True
                    break
            if flag != True:
                res+=1
        return res
