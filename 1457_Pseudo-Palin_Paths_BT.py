'''
Leetcode 1457. Pseudo-Palindromic Paths in a Binary Tree
Find # of root-leaf paths that can be rearranged into a palindrome.

DFS backtrack to check each path, maintain a set of path node values.
The set keeps node # that appear only odd times. A path is pseudo palindromic = set length is 0 or 1
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.path = []
        self.palin = set()
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, rt: TreeNode) -> None:
        # push rt to path
        # and eliminate/add rt.val to palindrome set if present/missing
        self.path.append(rt)
        if rt.val not in self.palin:
            self.palin.add(rt.val)
        else:
            self.palin.remove(rt.val)
        if rt.left:
            self.dfs(rt.left)
        if rt.right:
            self.dfs(rt.right)
        # at leaf node, palindrome path means palin holds 0 or 1 value.
        if not rt.left and not rt.right and len(self.palin) <= 1:
            self.res += 1
        # pop rt from path
        # and reverse(same operation) the palindrom node checking state
        self.path.pop()
        if rt.val not in self.palin:
            self.palin.add(rt.val)
        else:
            self.palin.remove(rt.val)
        return