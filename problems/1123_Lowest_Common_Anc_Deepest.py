'''
Leetcode 1123. Lowest Common Ancestor of Deepest Leaves
Find the neareast common ancestor of all deepest leaves of a BT

Method 1, dfs post-order find paths to deepest nodes, compare them for LCA
DFS recursively dig for the deepest leaves and their paths, should be of the same length
Then find the farthest common node in these paths.
Time O(n), Space O(log(n)) worst case O(n)

Method 2, refine on method 1, dfs post-order returning only potential LCA and depth
Same idea as Method 1, but we don't need to collect entire paths to deepest node
For each node, as it is potential LCA, just decide returning itself, or some potential LCA of its subtree
Time O(n), Space O(1) not considering call stack
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    # method 1, dfs post-order find paths to deepest nodes, compare them for LCA
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # find the path to deepest leaves
        self.paths, self.path = [], []
        self.depth = -1
        self.dfsDeepest(root, 0)

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

    
    # method 2, refind on method 1, decide return self node, or LCA node from subtree
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # post order dfs traversal, return (LCA of deepest nodes in subtree, depth of subtree)
        def post_order(rt: Optional[TreeNode]) -> tuple:
            if not rt:
                return rt, 0
            # get lca and depth of both subtrees
            left_lca, d1 = post_order(rt.left)
            right_lca, d2 = post_order(rt.right)
            # subtree depth the same, thus both of them contain some local deepest leaves
            # rt must be LCA of current subtree's group of deepest leaves
            if d1 == d2:
                return rt, d1+1
            # left subtree is deeper, its LCA should be returned
            if d1 > d2:
                return left_lca, d1+1
            # same for right subtree is deeper
            return right_lca, d2+1

        return post_order(root)[0]