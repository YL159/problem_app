'''
1038. Binary Search Tree to Greater Sum Tree
Given a BST, return the tree where each node value = sum(all values in the BST that >= node value)

1. Intuitively, we can extract the in-order # array from BST, the sum of all greater values are just suffix sum of the array
Then make a node value -> suffix sum projection on the original BST.

Many solutions involve global/class variable/array to hold the current sum.

A better way is to progressively collect the sum of reversed in-order traversal, and change each node simultaneously.
Because for reversed in-order traversal, visiting a node means all the greater nodes have been visited.
Why don't we also collect the sum of those visited greater nodes in the mean time?

2. define a reverse in-order recursive function, receive the sum of all values greater than argument node rt,
and return the sum of all values including the subtree of node rt
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.reverseInOrder(root, 0)
        return root

	# immitate in-order + suffix sum procedure.
	# make a reversed in-order traversal, keep current sum.
    def reverseInOrder(self, rt: TreeNode, s: int) -> int:
        if not rt:
            return s
        # visit & change right subtree, then visit rt
        rt.val += self.reverseInOrder(rt.right, s)
        # finally visit left subtree with updated sum
        return self.reverseInOrder(rt.left, rt.val)
