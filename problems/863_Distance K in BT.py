'''
Leetcode 863. All Nodes Distance K in Binary Tree
Find all nodes that are k distance to target node in a BT

Except for most of the solutions converting the BT into a graph and use target as center for BFS,

Here use DFS backtrack to find the path to the target,
and examine each parent and their other subtree with remaining distance.
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = []
        self.findPath(root, target.val, path)
        
        res = []
        n = len(path)-1
        for i, node in enumerate(path):
            # treat target node and possible end parent node
            if n-i == k or n-i == 0:
                self.disK(node, k-n+i, res)
            # treat other parents within the path
            elif n-i < k:
                for x in (node.left, node.right):
                    if x and x.val != path[i+1].val:
                        self.disK(x, k-n+i-1, res)
            # skip far parents if any
        return res

    # dfs find the target and the path nodes to it
    def findPath(self, r: TreeNode, t: int, arr: List[TreeNode]) -> bool:
        if not r:
            return False
        arr.append(r)
        if r.val == t or self.findPath(r.left, t, arr) or self.findPath(r.right, t, arr):
            return True
        arr.pop()
        return False
        
    # bfs check all children of given parent with k distance to target
    def disK(self, parent: TreeNode, k: int, result: List[int]) -> None:
        layer1, layer2 = [parent], []
        while k > 0:
            for node in layer1:
                if node.left:
                    layer2.append(node.left)
                if node.right:
                    layer2.append(node.right)
            layer1, layer2 = layer2, []
            k -= 1
        for node in layer1:
            result.append(node.val)
