'''
Leetcode 987. Vertical Order Traversal of a Binary Tree
Tree root is column 0. A node's left/right child is -1/+1 to parent's column.
Return a list of list, outer list is in increasing order of column number
inner list holds node values from top to bottom of the same column, if multiple nodes on the same level, sort them.

Use DFS or BFS, determine current node's depth and column number
store info in column list's correct position, depth as dictionary key
Combine the left/right column lists, flatten the inner dict to lists
Time O(n), Space O(n)

Similar question: Top down view of a tree
Return a list of visible node values as if looking down from the top of the tree.

Use each node's column and depth info to determine if this node is the 'top' visible node in a column.
If encounter a node of some existing column but with smaller depth, replace the previous record.
Thus we only need left/right column lists, with (node.val, depth) tuple, instead of dict recording all nodes of a column.
Finally the same flatten the combined lists.
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # pre-order traversal to collect each node's depth & offset from parent's
        rcol, lcol = [], [{0: [root.val]}]

        def dfs(rt: Optional[TreeNode], dep: int, col: int) -> None:
            if not rt:
                return
            col_list, c = rcol, col
            if col < 0:
                col_list, c = lcol, -col
            if c == len(col_list):
                col_list.append({dep: [rt.val]})
            elif dep in col_list[c]:
                col_list[c][dep].append(rt.val)
            else:
                col_list[c][dep] = [rt.val]
            dfs(rt.left, dep+1, col-1)
            dfs(rt.right, dep+1, col+1)
        
        dfs(root, 0, 0)
        ful_list = lcol[1:][::-1]
        ful_list.extend(rcol)
        res = []
        for book in ful_list:
            col = []
            # BFS can avoid sorting keys(depth), use list instead of dict
            for k in sorted(book.keys()):
                col.extend(sorted(book[k]))
            res.append(col)
        return res

