class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int l = grid.length;
        int w = grid[0].length;
        int result = 0;
        for (int i = 0; i < l; i += 1) {
            for (int j = 0; j < w; j += 1) {
                result = Math.max(result, dfs(grid, i, j, l, w, 0));
            }
        }
        return result;
    }

    int dfs(int[][] grid, int i, int j, int l, int w, int area) {
        if (i < 0 || j < 0 || i >= l || j >= w || grid[i][j] == 0) {
            return area;
        }
        grid[i][j] = 0;
        area += 1;
        area = dfs(grid, i - 1, j, l, w, area);
        area = dfs(grid, i, j - 1, l, w, area);
        area = dfs(grid, i + 1, j, l, w, area);
        area = dfs(grid, i, j + 1, l, w, area);
        return area;
    }
}