class Solution {
public:
    int m, n;
    vector<vector<bool>> vis;

    void dfs(int r, int c, vector<vector<char>>& grid) {
        
        vis[r][c] = true;


        if (r - 1 >= 0) {
            if (grid[r - 1][c] == '1' && !vis[r - 1][c]) {
                dfs(r - 1, c, grid);
            }
        }

        if (r + 1 < m) {
            if (grid[r + 1][c] == '1' && !vis[r + 1][c]) {
                dfs(r + 1, c, grid);
            }
        }

        if (c - 1 >= 0) {
            if (grid[r][c - 1] == '1' && !vis[r][c - 1]) {
                dfs(r, c - 1, grid);
            }
        }

        if (c + 1 < n) {
            if (grid[r][c + 1] == '1' && !vis[r][c + 1]) {
                dfs(r, c + 1, grid);
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        
        m = grid.size();
        n = grid[0].size();

        vis = vector<vector<bool>>(m, vector<bool>(n, false));

        int ct = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {

                if (grid[r][c] == '0')
                    continue;

                if (vis[r][c])
                    continue;

                dfs(r, c, grid);
                ct++;
            }
        }

        return ct;
    }
};
