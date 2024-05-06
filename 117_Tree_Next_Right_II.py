'''
117. Populating Next Right Pointers in Each Node II
For each node in a binary tree, populate 'next' pointer to its right neighbor in the same layer

Other than BFS using O(n) space, here keep finished layer's head reference and O(1) space generate current layer's pointers
'''

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # assume layer "pre" is next-complete
        pre_head = root
        # outer loop for each pre layer
        while pre_head:
            pre = pre_head
            cur = None
            # find the start of current layer
            # creating dummy head to avoid lone start node self referencing later
            while not cur and pre:
                if pre.left or pre.right:
                    cur = Node(-1)
                else:
                    pre = pre.next
            pre_head = cur
            # grow the cur.next linked nodes
            while pre:
                for x in (pre.left, pre.right):
                    if x:
                        cur.next = x
                        cur = x
                pre = pre.next
            if pre_head:
                pre_head = pre_head.next
        return root
            
