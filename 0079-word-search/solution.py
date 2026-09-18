class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS,COLS = len(board), len(board[0])
        visited = [[False] * COLS for x in range(ROWS)]

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c<0 or r>= ROWS or c >=COLS or word[i] != board[r][c] or visited[r][c]:
                return False
            
            visited[r][c] = True

            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            visited[r][c] = False
            return res
        
        for x in range(ROWS):
            for y in range(COLS):
                if dfs(x,y,0):
                    return True
        return False
