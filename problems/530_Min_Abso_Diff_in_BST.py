'''
Leetcode 530. Minimum Absolute Difference in BST
Find the min absolute difference between any 2 different nodes in a BST

Observation:
BST has left subtree < root value < right subtree
Thus the min absolute diff between 2 nodes must come from:
    root value - max(left subtree) or
    min(right subtree) - root value
Otherwise any other nodes can only be much smaller or larger compared to current root.

Method 1, in-order traversal, neighbor diff
In-order traversal naturally gets sorted value array of nodes, thus min diff comes from neighbor diffs
Time O(n), Space O(n) if using additional node value array.

Method 2, post-order traversal, compare only root and max(left subtree) and min(right subtree)
Time O(n), Space O(1)
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # method 1, in-order traversal
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(ro: TreeNode, inor: List[int]) -> None:
            if ro.left:
                inorder(ro.left, inor)
            inor.append(ro.val)
            if ro.right:
                inorder(ro.right, inor)
            return
        
        values = []
        inorder(root, values)
        result = abs(values[1] - values[0])
        for i in range(1, len(values)):
            result = min(values[i] - values[i-1], result)
        return result
    
    # method 2, post-order traversal
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # for BST, min difference happens between:
        # root and left_subtree_right_most_node
        # root and right_subtree_left_most_node
        # post order traversal, time O(n), space O(1)
        return self.post_order(root)[0]

    # return (subtree best result, subtree left most node value, subtree right most node value)
    def post_order(self, rt: TreeNode) -> tuple:
        res1, ll, ldiff = float('inf'), rt.val, float('inf')
        res2, rdiff, rr = float('inf'), float('inf'), rt.val
        if rt.left:
            res1, ll, lr = self.post_order(rt.left)
            ldiff = rt.val - lr
        if rt.right:
            res2, rl, rr = self.post_order(rt.right)
            rdiff = rl - rt.val
        return min(res1, res2, ldiff, rdiff), ll, rr