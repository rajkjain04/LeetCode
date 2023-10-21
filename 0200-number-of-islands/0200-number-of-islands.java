import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null) {
            return 0;
        }

        int islands = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    islands += 1;
                    bfs(grid, r, c);
                }
            }
        }

        return islands;
    }

    public boolean isValid(int r, int c, char[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;

        return r >= 0 && r != ROWS && c >= 0 && c != COLS && grid[r][c] != '0';
    }

    public void bfs(char[][] grid, int r, int c) {

        Queue<int[]> queue = new LinkedList<>();
        grid[r][c] = '0';

        queue.add(new int[]{r, c});

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0];
            int col = cell[1];

            int[][] neighbours = new int[][]{new int[]{row + 1, col}, new int[]{row - 1, col}, new int[]{row, col + 1}, new int[]{row, col - 1}};

            for (int[] neighbour: neighbours) {
                int newRow = neighbour[0];
                int newCol = neighbour[1];

                if (isValid(newRow, newCol, grid)) {
                    queue.add(new int[]{newRow, newCol});
                    grid[newRow][newCol] = '0';
                }
            }
        }
    }
}