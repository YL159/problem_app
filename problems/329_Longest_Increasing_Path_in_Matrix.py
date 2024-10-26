'''
Leetcode 329. Longest Increasing Path in a Matrix
Find the length of longest strictly increasing path in a matrix.
A path contains only up/down/left/right walks, and within matrix boundaries

Most solutions uses recursive DFS. Here is an iterative BFS solution
BFS starts from smallest cells, then iteratively check unvisited larger cells
Also initialize score board for each cell's state of visit, and smaller neighbor indegree

Starts from smallest cells, propagate to their larger neighbors's scores
But only those larger neighbors whose indegree is exhausted will be "mature" enough,
to propagate their scores to the next iteration.
Thus saving time from propagating a smaller score to the end of future paths.

Time O(m*n), space O(m*n)
'''
from typing import List
import collections

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # cell value: set of coordinates
        book = collections.defaultdict(set)
        # each cell: [max path, smaller neighbor cells count]
        score = []
        for i in range(m):
            score.append([])
            for j in range(n):
                score[i].append([-1, 0])
                book[matrix[i][j]].add((i, j))
                candi = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for x, y in candi:
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if matrix[x][y] < matrix[i][j]:
                        score[i][j][1] += 1

        for k in sorted(book.keys()):
            cur, nex = set(), set()
            for i, j in book[k]:
                if score[i][j][0] == -1:
                    score[i][j][0] = 1
                    cur.add((i, j))
            while cur:
                for i, j in cur:
                    candi = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                    for x, y in candi:
                        if x < 0 or x >= m or y < 0 or y >= n:
                            continue
                        if matrix[x][y] > matrix[i][j]:
                            score[x][y][0] = max(score[x][y][0], score[i][j][0]+1)
                            score[x][y][1] -= 1
                            # propagate only when larger cell's all smaller neighbors yield some result
                            if score[x][y][1] == 0:
                                nex.add((x, y))
                cur, nex = nex, set()
        return max([max(row) for row in score])[0]