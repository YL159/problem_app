'''
Leetcode 971. Flip Binary Tree To Match Preorder Traversal
Given a BT and a preorder traversal array, find a list of roots to flip their subtrees to match the preorder array,
or return [-1]

Make in-order traversal on the tree, thus the index of voyage is +1 increasing while in-order traversal.
Check each root.value equal to current voyage number. Swap left/right if mismatch.
And recursively traverse left then right subtree, in order for in-order.
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.res = []
        self.index = 0
        self.voyage = voyage

        if self.inOrder(root):
            return self.res
        else:
            return [-1]                    
            
    # in-order check subtree rt, return True if voyage possible, else False
    def inOrder(self, rt: Optional[TreeNode]) -> bool:
        if not rt:
            return True
        if rt.val != self.voyage[self.index]:
            return False
        self.index += 1
        cur = rt.left if rt.left else rt.right
        if cur and cur.val != self.voyage[self.index]:
            self.res.append(rt.val)
            # swap the subtrees to match voyage
            rt.left, rt.right = rt.right, rt.left
        return self.inOrder(rt.left) and self.inOrder(rt.right)