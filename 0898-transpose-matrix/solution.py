class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = len(matrix)
        col = len(matrix[0])
        temp = [[0] * row for x in range(col)] 
        for x in range(row):
            for y in range(col):
                temp[y][x] = matrix[x][y]
        return temp
