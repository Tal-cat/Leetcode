class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # START
        # Dynamic programming
        m = len(grid)
        n = len(grid[0])
        # define memo for storage, init = -1
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        def dp(grid: List[List[int]], i: int, j: int) -> int:
            # base case
            if i == 0 and j == 0:
                return grid[0][0]
            # index out of bound, return inf so it won't influence min
            if i < 0 or j < 0:
                return float('inf') 
            # Already calculated
            if memo[i][j] != -1:
                return memo[i][j]
            # memeory result to get rid of Time Limit Exceeded
            memo[i][j] = min(dp(grid, i - 1, j), dp(grid, i, j-1)) + grid[i][j]

            return memo[i][j]
        
        return dp(grid, m - 1, n - 1)
