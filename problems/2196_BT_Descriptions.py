'''
Leetcode 2196. Create Binary Tree From Descriptions
Create a binary tree from a list of [parent, child, isLeft] tuples.

Create a {parent:[left, right]} dictionary, find the root value and DFS populate the childrens
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childrens = set()
        # Dictionary of parent: [left, right], value 0 is empty child
        for a, b, c in descriptions:
            childrens.add(b)
            if a not in nodes:
                nodes[a] = [0, 0]
            if c:
                nodes[a][0] = b
            else:
                nodes[a][1] = b
        # root value won't appear in children values
        roots = set(nodes.keys())
        root_val = list(roots - childrens)[0]

		# recursively populate the nodes according to nodes dict
        def create(rt: int) -> Optional[TreeNode]:
            if rt == 0:
                return None
            if rt not in nodes:
                return TreeNode(rt)
            node = TreeNode(rt)
            l, r = nodes[rt]
            node.left = create(l)
            node.right = create(r)
            return node
        
        return create(root_val)