'''
Leetcode 576. Out of Boundary Paths
Given a board of m*n, and start position of the ball, and max moves.
Find the total number of paths that eventually get the ball off the board.

Use DFS recursion and DP on every cell's off-board path count for x moves.
Base case: 1 move off board = sum(neighbors off board)
Recursive case: Cell's x move off board paths = sum(neighbor's x-1 move off board paths)
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # DFS DP, or update the whole matrix for maxMove v. All seems O(vmn)
        # matrix of {move: # of path off board within move}
        self.dp = [[{} for _ in range(n)] for _ in range(m)]
        self.m, self.n = m, n
        total = 0
        for i in range(1, maxMove+1):
            total += self.recur(i, startRow, startColumn)
        return total % (10**9+7)

    def recur(self, move: int, row: int, col: int) -> int:
        if move in self.dp[row][col]:
            return self.dp[row][col][move]
        
        four = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        candi = []
        for r, c in four:
            if 0 <= r < self.m and 0 <= c < self.n:
                candi.append((r, c))
        # if query 1 move, return # of neighbor off board cells.
        if move == 1:
            self.dp[row][col][1] = 4 - len(candi)
            return 4 - len(candi)
        
        res = 0
        # query x move is the sum of query x-1 move for neighbor valid cells
        for r, c in candi:
            res += self.recur(move-1, r, c)
        self.dp[row][col][move] = res
        return res