'''
Leetcode 919. Complete Binary Tree Inserter
Make a BT inserter class that initialize when given the root of a complete BT
and insert new nodes to the complete BT

1. Intuitive & simple BFS deque method:
Time O(n) initialize, O(1) insertion. Space O(n)
Maintain deque of the last full row & last row, queue left is the current parent.


2. Here is candidate path based method:
Time O(log(n)^2) initialize, O(log(n)) insertion. Space O(log(n))

Initialization takes nested binary search on current path code
modify the path till the code represents the last node of the BT
Thus the insertion point <=> Path code increment by 1

At insertion, keep track of the binary path code to the next available insertion point.
The next available point <=> also path code increment by 1
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        # saves the path code of current insertion point
        # 0 -> go left, 1 -> go right
        # next insertion is 6->110->1,[1,0]
        self.path = []
        l = root
        while l.left:
            self.path.append(0)
            l = l.left
        # O(log(n)^2) time to find the path to current insertion point
        for i in range(len(self.path)):
            self.path[i] = 1
            count, _ = self.travel()
            if count < len(self.path):
                self.path[i] = 0
        # next insertion point is the next path code
        self.add_1()
        _, self.tail = self.travel()

    # O(log(n)) time to update the tree
    def insert(self, val: int) -> int:
        res = self.tail.val
        self.add_1()
        if not self.tail.left:
            self.tail.left = TreeNode(val)
        else:
            self.tail.right = TreeNode(val)
            _, self.tail = self.travel()
        return res

    def get_root(self) -> Optional[TreeNode]:
        return self.root
    
    # add 1 to the path code
    def add_1(self) -> None:
        carry = 1
        for i in range(len(self.path)-1, -1, -1):
            s = self.path[i] + carry
            self.path[i] = s % 2
            carry = s // 2
        if carry:
            self.path.append(0)

    # get the (depth, last node) of self.path
    def travel(self) -> tuple:
        count = 0
        cur = self.root
        for j in range(len(self.path)):
            if self.path[j] == 0 and cur.left:
                cur = cur.left
            elif self.path[j] == 1 and cur.right:
                cur = cur.right
            else:
                break
            count += 1
        return (count, cur)


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()