'''
Leetcode 230. Kth Smallest Element in a BST
Given a BST, find kth smallest element.

In-order traverse while counting skipped smaller nodes till kth. O(n)
But above solution is not optimum if frequent node add/delet operations on BST

We want to pre-compute a 'smaller-than' property for each node, which helps reduce repeated subtree counting

Add an attr of left_subtree_node_count on each node. Initially this takes O(n) time
Each subsequent node add/delete operations take O(log(n)) time:
	Binary search for the target node, keep search path.
	Update (+/- 1) each parent node's lsub if the change occurs from its left subtree

Finding kth smallest node also takes O(log(n)):
	Binary search for the kth by comparing k with node.lsub + 1
	If equal => current node is the kth smallest node
	If smaller => kth node must be in current node's left subtree
	If bigger => update the remaining count k' and search right subtree
'''
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None, lsub=0):
        self.val = val
        # add attr: # of nodes in its left subtree
        self.lsub = lsub
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # post-order O(n) update each node with left subtree node count
        def update_left(rt: Optional[TreeNode]) -> int:
            if not rt:
                return 0
            rt.lsub = update_left(rt.left)
            right = update_left(rt.right)
            return rt.lsub + right + 1

        # O(logn) binary search for the kth node
        def recur(rt: Optional[TreeNode], t:int) -> int:
            if t == rt.lsub + 1:
                return rt.val
            if t <= rt.lsub:
                return recur(rt.left, t)
            return recur(rt.right, t-rt.lsub-1)

        update_left(root)
        return recur(root, k)
            