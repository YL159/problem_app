'''
Leetcode 934. Shortest Bridge
Given a matrix of only 1/0, 1=land, 0=sea. There are exactly 2 islands.
Find min # of sea cells to flip as land, to connect these 2 islands.

From one island's shore line, BFS expand untill meeting the other island.
BFS guarantees shortest bridge.

Mark 1st island as other marker in order not to revisit it.
Time O(n^2), Space O(n^2)
'''

from typing import List

import collections

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # from 1 island's outline, BFS extend to the other island
        # BFS depth is smallest bridge
        # outline cell must have at least one neighbor of 0
        n = len(grid)
        island = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    island = True
                    break
            if island:
                break
        cur = collections.deque()
        cur.append((i, j))
        grid[i][j] = 2
        shore = {(i, j)}

        # find current island's outline shore, visited cell marked as 2
        while cur:
            i, j = cur.popleft()
            outline = False
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        # mark land as 2, prevent revisit and re-append
                        grid[x][y] = 2
                        cur.append((x, y))
                    elif grid[x][y] == 0:
                        outline = True
            if outline:
                shore.add((i, j))

        # BFS on island "2" cells
        count = 0
        _shore = set()
        while shore:
            for x, y in shore:
                for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= a < n and 0 <= b < n:
                        if grid[a][b] == 1:
                            return count
                        if grid[a][b] == 0:
                            grid[a][b] = 2
                            _shore.add((a, b))
            shore, _shore = _shore, set()
            count += 1
