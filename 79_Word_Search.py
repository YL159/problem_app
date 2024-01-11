'''
Leetcode 79 Word Search
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(ws, i, j) -> bool:
            # DFS from current (i,j) position
            if not ws:
                return True
            # trim for valid neighbor coordinates
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in neighbors.copy():
                if x < 0 or x >= m or y < 0 or y >= n:
                    neighbors.remove((x, y))
            # get valid candidates for next recursion
            cand = []
            for x, y in neighbors:
                if not visit[x][y] and board[x][y] == ws[0]:
                    cand.append((x, y))
            # DFS with visite map back track
            for x, y in cand:
                visit[x][y] = 1
                if search(ws[1:], x, y):
                    return True
                visit[x][y] = 0
            return False

        m, n = len(board), len(board[0])
        # maintain only 1 visit map, thus DFS
        visit = [ [0 for i in range(n)] for j in range(m) ]
        candidates = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    candidates.append((i, j))
        for candidate in candidates:
            i, j = candidate
            visit[i][j] = 1
            if search(word[1:], i, j):
                return True
            visit[i][j] = 0
        return False