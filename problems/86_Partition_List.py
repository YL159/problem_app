'''
Leetcode 86. Partition List
Go through the linked list and group nodes with value < x before nodes >= x.
Then concatenate them in original order.

Maintain 2 linked list of lesser and no-lesser than x in traversing order/
Then concatenate them.
Time O(n), Space O(1)
'''
class Solution:
    def partition(self, head, x: int):
        if not head:
            return head
        less_h, less_t = None, None
        more_h, more_t = None, None
        node, pre = head, head
        while node:
            # collect less than x nodes sequentially
            if node.val < x:
                if not less_h:
                    less_h = node
                elif pre.val >= x:
                    less_t.next = node
                less_t = node
            # collect more than x nodes sequentially
            else:
                if not more_h:
                    more_h = node
                elif pre.val < x:
                    more_t.next = node
                more_t = node
            pre = node
            node = node.next
        # construct the whole list
        if more_h:
            more_t.next = None
        if less_t:
            less_t.next = more_h
            res = less_h
        else:
            res = more_h
        return res
    