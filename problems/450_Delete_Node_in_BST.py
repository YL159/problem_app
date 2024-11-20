'''
Leetcode 450. Delete Node in a BST
Given the root of a BST, delete a node with value = key

To delete a node in BST and maintain its structure, the node to delete must be replaced by:
	Largest node in its left subtree
	Or smallest node in its right subtree (choice here)
And also maintain the modified subtree's structure.

Thus we can see there is a recursive structure: Delete some node(key) as root in a subtree.
If root has no right subtree:
	using left subtree root to replace it won't break BST structure.
else:
	find the value of smallest node in right subtree, resolve right subtree, and make that node new root
Always return current root for higher stack calls, thus to reconnect the changed nodes.

Time O(log(n)), space in stack O(1), use only original node obj with their initial values.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # substitude with largest smaller node or smallest larger node (here)
        # this function satisfies recursive structure
        if not root:
            return None
        if root.val == key:
            if not root.right:
                return root.left
            else:
                larger = root.right
                while larger.left:
                    larger = larger.left
                # the subtree containint new root (larger) is already resolved
                # thus safely update this node
                larger.right = self.deleteNode(root.right, larger.val)
                larger.left = root.left
                return larger
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root