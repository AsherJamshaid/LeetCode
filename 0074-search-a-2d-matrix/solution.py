class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        found = False 

        for x in range(len(matrix)):
            for y in range(len(matrix[0])): 
                if matrix[x][y] == target:
                    found = True
                    break  
            if found:
                break  

        return found

