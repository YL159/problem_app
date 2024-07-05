'''
Leetcode 951. Flip Equivalent Binary Trees
Check if 2 trees are equivalent if several nodes have their respective children left-right flipped.

Since all node values are unique, for the 2 children (including empty node) of a node, sort by value (None for -1).
Compare children sequentially for 2 roots, instead of cross compare like:
(root1.left, root2.left) and (root1.right, root2.right) or (root1.left, root2.right) and (root1.right, root2.left)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 and root2:
            if root1.val != root2.val:
                return False
            # use unique node value to avoid subtree cross recursive calls
            one = [root1.left, root1.right]
            one.sort(key=lambda node: node.val if node else -1)
            two = [root2.left, root2.right]
            two.sort(key=lambda node: node.val if node else -1)
            return self.flipEquiv(one[0], two[0]) and self.flipEquiv(one[1], two[1])
        elif root1 and not root2 or not root1 and root2:
            return False
        else:
            return True
        