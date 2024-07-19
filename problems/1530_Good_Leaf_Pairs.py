'''
Leetcode 1530. Number of Good Leaf Nodes Pairs
For each pair of leaf nodes, if shortest distance is no greater than given distance, they count as 1 good pair.

1. Reuse 112 lowest common ancestor method, find paths to all leaves, and check node difference index to find distance.
Slow because if tree is deep, each check between 2 paths starts from root node.

2. Post order traverse the tree with depth information.
At each root, only pair left leaves with right leaves because potential pairs within left/right leaves are handled in recursive calls,
and only the shortest path betwee 1 left and 1 right leaf pass through current root.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # 1. similar to lowest common ancestor problem.
        # The shortest path must go throughthe lca
        # slower because in nested loop we always check from root.
    #     self.path = []
    #     self.paths = []
    #     self.dfsPath(root)
    #     if len(self.paths) < 2:
    #         return 0
    #     res = 0
    #     for i in range(len(self.paths)-1):
    #         for k in range(i+1, len(self.paths)):
    #             cur, nex = self.paths[i], self.paths[k]
    #             c, n = len(cur), len(nex)
    #             for j in range(min(c, n)):
    #                 if cur[j] != nex[j]:
    #                     res += c+n-2*j <= distance
    #                     break
    #     return res
    #
    # def dfsPath(self, rt: Optional[TreeNode]) -> None:
    #     self.path.append(rt)
    #     if rt.left:
    #         self.dfsPath(rt.left)
    #     if rt.right:
    #         self.dfsPath(rt.right)
    #     if not rt.left and not rt.right:
    #         self.paths.append(self.path.copy())
    #     self.path.pop()

        # 2. post order traverse using depth info
        self.path = []
        self.res = 0
        self.distance = distance
        self.dfsPostOrder(root, 1)
        return self.res
    # Collect leaf depth info from left/right subtree, and cross check
    # because only shortest path between left leaf and right leaf can pass rt
    def dfsPostOrder(self, rt: Optional[TreeNode], depth: int) -> list:
        if not rt:
            return []
        l = self.dfsPostOrder(rt.left, depth + 1)
        r = self.dfsPostOrder(rt.right, depth + 1)
        if not l and not r:
            return [depth]
        if not l:
            return r
        if not r:
            return l
        # print(depth, l, r)
        for n in l:
            for m in r:
                self.res += n+m-2*depth <= self.distance
        return l + r