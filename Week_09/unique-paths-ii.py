class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            obstacleGrid[i][0] = (1 - obstacleGrid[i][0]) * obstacleGrid[i - 1][0]
        for j in range(1, n):
            obstacleGrid[0][j] = (1 - obstacleGrid[0][j]) * obstacleGrid[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]