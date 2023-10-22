import java.util.LinkedList;
import java.util.Queue;

class Solution {

    public boolean isValid(int[][] grid, int r, int c) {
        int ROWS = grid.length;
        int COLS = grid[0].length;

        return r >= 0 && r != ROWS && c >= 0 && c != COLS && grid[r][c] == 1;

    }
    public int orangesRotting(int[][] grid) {
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;
        int time = 0;

        int ROWS = grid.length;
        int COLS = grid[0].length;

        for(int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 2) {
                    queue.add(new int[]{r, c});
                }
                else if (grid[r][c] == 1) {
                    fresh += 1;
                }
            }
        }

        while (!queue.isEmpty() && fresh > 0) {

            int queueLength = queue.size();

            for (int i = 0; i < queueLength; i++) {
                int[] cell = queue.poll();
                int r = cell[0];
                int c = cell[1];

                int[][] neighbours = new int[][]{new int[]{r + 1, c}, new int[]{r - 1, c}, new int[]{r, c + 1}, new int[]{r, c - 1}};

                for (int[] neighbour: neighbours ) {
                    int row = neighbour[0];
                    int col = neighbour[1];

                    if (isValid(grid, row, col)) {
                        queue.add(new int[]{row, col});
                        fresh -= 1;
                        grid[row][col] = 2;
                    }
                }
            }

            time += 1;
        }

        if (fresh > 0) {
            return -1;
        } else {
            return time;
        }
    }
}