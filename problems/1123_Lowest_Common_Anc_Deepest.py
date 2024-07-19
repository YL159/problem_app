'''
Leetcode 1123. Lowest Common Ancestor of Deepest Leaves
Find the neareast common ancestor of deepest leaves of a BT

DFS recursively dig for the deepest leaves and their paths, should be of the same length
Then find the farthest common node in these paths.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # find the path to deepest leaves
        self.paths, self.path = [], []
        self.depth = -1
        self.dfsDeepest(root, 0)
        for x in self.paths:
            print([y.val for y in x])
        print(self.depth)

        # for the deepest leaves, get the last same node in their paths
        first = self.paths[0]
        for i in range(len(first)):
            tmp = first[i].val
            res = True
            for pth in self.paths:
                res &= tmp == pth[i].val
            if not res:
                return first[i-1]
        return first[-1]

    def dfsDeepest(self, rt: Optional[TreeNode], dep: int) -> None:
        self.path.append(rt)
        if rt.left:
            self.dfsDeepest(rt.left, dep+1)
        if rt.right:
            self.dfsDeepest(rt.right, dep+1)
        if not rt.left and not rt.right:
            if dep == self.depth:
                self.paths.append(self.path.copy())
            elif dep > self.depth:
                self.depth = dep
                self.paths = [self.path.copy()]
        self.path.pop()