'''
Leetcode 652. Find Duplicate Subtrees
return root of duplicate subtrees, 1 for each type of duplicate. Duplicate subtrees has the same sturcture & node values


Post order traverse the tree, construct a string representation (1st hash) of each subtree using post order concatenation.
Store these codes in dictionary for duplicate check (2nd hash)
Include empty children of any valid nodes to break the undeterministic property of post order traversal alone.
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # encrypt every subtree into a string or number, i.e. hash it
        # create a dictionary of {rt.val : hashcode set}
        self.book = {}
        # create a dictionary to record duplicate as {hashcode: node}
        self.rep = {}
        if root.left:
            self.hashFindPostOrder(root.left)
        if root.right:
            self.hashFindPostOrder(root.right)
        return list(self.rep.values())

    def hashFindPostOrder(self, rt: TreeNode) -> str:
        code = ''
        if not rt.left and not rt.right:
            # handle leaf nodes
            code = str(rt.val)
        else:
            # encode 'null' value ('n') if any sibling node or rt
            l, r = 'n', 'n'
            if rt.left:
                l = self.hashFindPostOrder(rt.left)
            if rt.right:
                r = self.hashFindPostOrder(rt.right)
            code = ','.join([l, r, str(rt.val)])
        # new rt value creates a new set of codes all rooted at rt.val
        if rt.val not in self.book:
            self.book[rt.val] = {code}
        # a visited rt.val and has the same code seen before, duplicate!
        elif code in self.book[rt.val]:
            self.rep[code] = rt
        # new code rooted at rt.val, add to rt.val code collection
        else:
            self.book[rt.val].add(code)
        return code
