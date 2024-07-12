'''
Leetcode 2096. Step-By-Step Directions From a Binary Tree Node to Another
Given a BT, start and destination node value, find the path direction from start to dest.

Start from root, find path to both start and dest nodes.
Check and remove the same prefix from paths, and combine for the real path from start to dest.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # similar to lowest common ancestor. Find path and check common ancestor.
        self.start, self.dest = None, None
        self.startValue, self.destValue = startValue, destValue
        self.path = []
        self.dfs(root)
        i = 0
        while i < min(len(self.start), len(self.dest)):
            if self.start[i] != self.dest[i]:
                break
            i += 1
        self.start, self.dest = ['U']*(len(self.start) - i), self.dest[i:]
        return ''.join(self.start + self.dest)

    def dfs(self, rt: TreeNode) -> None:
        if rt.val == self.startValue:
            self.start = self.path.copy()
        elif rt.val == self.destValue:
            self.dest = self.path.copy()
        if rt.left:
            self.path.append('L')
            self.dfs(rt.left)
            self.path.pop()
        if rt.right:
            self.path.append('R')
            self.dfs(rt.right)
            self.path.pop()
        return