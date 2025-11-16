'''
Leetcode 222. Count Complete Tree Nodes
Given a complete binary tree, find its total # of nodes.

Method 1, O(n) time BFS or DFS

Method 2, binary search for the ending point of last layer
Since the last layer's nodes are all on the left, and right is empty:
	perfect case for binary searching this breaking point
	=> left leaf nodes have depth k, right leaf nodes have depth k-1
This requires altering the path from root to reach each testing leaf node
	=> using binary path choice configuration
    => optimize path choice with int's binary representation (bit extraction and path encoding)

Path -> int encoding:
e.g. root as layer 1. At layer 3, there are 2^2 = 4 nodes (including empty nodes)
	=> 0th node: left -> left : 00 = 0, 1st node: left -> right : 01 = 1
    2nd node: right -> left : 10 = 2, 3rd node: right -> right : 11 = 3
The node index corresponds to its path code, and the order of natural number increment.
Thus node count is related to path code

And also make a multi-functional tree traversal function
follow designated path code and return depth

Node count < 5E4 < 2^10 * 64 = 2^16, thus max depth is 16
Time O(log^2(n)), Space O(1) because of binary encoding
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # path code check right side depth
        config = (1 << 16) - 1
        rlvl = self.check_layer(root, config)
        # path code check left side depth
        config = 0
        lvl = self.check_layer(root, config)
        # node count of the perfect layers
        res = (1 << rlvl) - 1
        if lvl == rlvl:
            return res

        # last layer is not full, binary search for last node's path config
        l, r = 0, 1 << rlvl
        while l < r-1:
            mid = (l + r) // 2
            if self.check_layer(root, mid, rlvl-1) == lvl:
                l = mid
            else:
                r = mid
        return res + r

    # check the layer count for a specific path config
    def check_layer(self, rt: TreeNode, conf: int, lvl: int=15) -> int:
        cur = rt
        count = 0
        while cur:
            count += 1
            if lvl < 0:
                break
            # config has 1 at bit lvl, go right
            if conf & 1 << lvl:
                cur = cur.right
            else:
                cur = cur.left
            lvl -= 1
        return count
        