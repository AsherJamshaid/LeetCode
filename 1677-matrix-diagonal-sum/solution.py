class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        res = 0
        mid = n // 2

        for x in range(n):
            res += mat[x][x]            
            res += mat[x][n - 1 - x]   

        if n % 2 != 0:
            res -= mat[mid][mid]   

        return res

