class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        arr = []
        arr_A = []
        arr_B = []
        for x in range(len(A)):
            count = 0
            arr_A.append(A[x])
            arr_B.append(B[x])
            for y in range(len(arr_A)):
                if arr_A[y] in arr_B:
                    count+=1
            arr.append(count)
        return arr
