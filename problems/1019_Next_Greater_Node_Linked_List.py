'''
Leetcode 1019. Next Greater Node In Linked List
Given a linked list, return an array, arr[i] = next greater node value of the node at index i

Use monotonically decreasing stack to record (node value, position) see so far.
If current node value is greater than top of stack, pop it and update arr.
'''
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # time O(n), space O(n)
        res = []
        # monotonically decreasing stack
        stack = []
        cur = head
        idx = 0
        while cur:
            if stack and cur.val > stack[-1][0]:
                while len(res) < idx:
                    res.append(0)
                while stack and cur.val > stack[-1][0]:
                    _, i = stack.pop()
                    res[i] = cur.val
            stack.append((cur.val, idx))
            idx += 1
            cur = cur.next

        while len(res) < idx:
            res.append(0)
        return res