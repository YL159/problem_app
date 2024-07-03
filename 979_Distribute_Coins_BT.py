'''
Leetcode 979. Distribute Coins in Binary Tree
Make every node in a tree has exactly 1 coin. 1 step is moving 1 coin on 1 edge.

Use post-order traversal to collect subtree information. Upon visiting root of subtree:
1. Each 0 node in both subtree will require 1 more step to fulfill from root. But can be negated by excessive coins
2. Thus total steps from both subtree depends on the NET coin influx/outflow, plus both subtree's basis steps

Collecting this information on the way back to tree root, thus no class/global var needed.
Since coin # = # of nodes, self.postOrder(root) must return (0, total_steps)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # postorder
        return self.postOrder(root)[1]

    # post order traversal return: (# of zeros not fulfilled or excessive coins, # of steps to balance this subtree)
    def postOrder(self, rt: Optional[TreeNode]) -> tuple:
        if not rt:
            return 0, 0
        zleft, sleft = self.postOrder(rt.left)
        zright, sright = self.postOrder(rt.right)
        # negative zeros means excessive coins
        zeros = zleft + zright + 1 - rt.val
        # steps required to balance this subtree. influx/outflow all accounted
        steps = sleft + sright + abs(zeros)
        return zeros, steps