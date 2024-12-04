'''
Leetcode 1171. Remove Zero Sum Consecutive Nodes from Linked List
Given the head of a linked list, recursively remove any sub linked list that sum(node.val) = 0
Return 1 of valid result

Idea is to regard the list as a list of numbers, make prefix sum at each idx.
A prefix sum that was seen before, indicates the subarr in between has sum = 0, and need removal

Here we use raw manipulation of nodes, instead of converting to int array and rebuild LL hack.
Use pref dictionary, add/remove keys to maintain {prefix sum: stop node} structure

Time O(n), space O(n)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        dum = ListNode(0, head)
		# maintain pref dict for current prefix sum -> node
        pref = {0: dum}
        cur = head
        while cur:
            # cur: tail of potential removal sub LL
            s += cur.val
            if s not in pref:
                pref[s] = cur
                cur = cur.next
                continue
            # prev: previous node of h
            prev = pref[s]
            # h: head of removal sub LL
            h = prev.next
            # connect previous node to next node, discard node in between
            prev.next = cur.next
            cur.next = None
            # restore pref dict back to state of 1st encounter of sum s
            while h != cur:
                s += h.val
                del pref[s]
                h = h.next
            # add cur.val and s back to 1st encounter of sum s, cus sum(removed node val) = 0
            s += cur.val
            # cur is now back on track of visiting next new node
            cur = prev.next
        return dum.next
