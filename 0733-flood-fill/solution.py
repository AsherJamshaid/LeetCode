class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def dfs(i,j,initialColor,newColor,image):
            n = len(image)
            m = len(image[0])

            if i < 0 or j < 0:
                return
            if i>=n or j >= m:
                return
            if image[i][j] != initialColor:
                return

            image[i][j] = newColor
            dfs(i-1,j,initialColor,newColor,image)
            dfs(i+1,j,initialColor,newColor,image)
            dfs(i,j-1,initialColor,newColor,image)
            dfs(i,j+1,initialColor,newColor,image)
        initialColor = image[sr][sc]
        if(initialColor!=color):
            dfs(sr,sc,initialColor,color,image)
        return image
