import java.security.KeyPair;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int numIslands(char[][] grid) {
        int numberOfIslands = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;


        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    numberOfIslands += 1;
                    dfs(grid, r, c);
                }
            }
        }

        return numberOfIslands;
    }

    private void dfs(char[][] grid, int r, int c) {
        int ROWS = grid.length;
        int COLS = grid[0].length;

        if (r < 0 || r == ROWS || c < 0 || c == COLS || grid[r][c] == '0') {
            return;
        }

        grid[r][c] = '0';

        dfs(grid,r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}
