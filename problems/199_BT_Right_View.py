'''
LeetCode 199. Binary Tree Right Side View
BFS iterative layers
'''
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        cur, nex = [root], []
        # BFS get the right most value of each layer
        while cur:
            res.append(cur[-1].val)
            nex = []
            for node in cur:
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            cur = nex
        return res