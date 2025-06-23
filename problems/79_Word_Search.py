'''
Leetcode 79 Word Search
Find if target word exists in given char matrix as a valid connected up-down-left-right path.

Recursive DFS, mark current path with #, early exit.
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS from current (i,j) position
        def search(idx, i, j) -> bool:
            # guard exit conditions
            if word[idx] != board[i][j]:
                return False
            # word[idx] match board[i][j], move to next index
            char = board[i][j]
            board[i][j] = '#'
            idx += 1
            if idx == len(word):
                return True
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if search(idx, x, y):
                    return True
            board[i][j] = char
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if search(0, i, j):
                    return True
        return False