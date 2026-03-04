class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(mat)        
        n = len(mat[0])  
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 1:
                    flag1 = False
                    flag2 = False
                    for z in range(m): #column k lye
                        if z == x:
                            continue
                        elif mat[z][y] == 1:
                            flag1 = True
                    for i in range(n): #row k lye
                        if i == y:
                            continue
                        elif mat[x][i] == 1:
                            flag2 = True
                    if flag1 == False and flag2 == False:
                        count+=1
        return count
