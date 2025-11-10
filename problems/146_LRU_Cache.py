'''
Leetcode 146. LRU Cache
Least Recently Used Cache implementation.
Least recently used(get/put) key should be removed, and in accessible, when new key-value comes and over capacity
Get/put should be O(1) time.

Use doubly linked list to make the operations O(1) time.
Recently accessed key nodes should be put to the top of the list.
If over capacity, least recently used node (last node) should be removed.
Also use node.key <-> map[key] to cross reference, keep track of capacity and cached nodes.
'''
class LRUCache:

    class Node:
        def __init__(self, key=0, val=0, pre=None, nex=None):
            self.key = key
            self.val = val
            self.pre = pre
            self.nex = nex

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dummy = self.Node(-1, -1)
        self.last = self.Node(-1, -1, pre=self.dummy)
        self.dummy.nex = self.last
        self.book = {}

    def get(self, key: int) -> int:
        if key not in self.book:
            return -1
        node = self.book[key]
        self._to_top(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.book:
            node = self.book[key]
            node.val = value
        else:
            node = self.Node(key, value)
            if len(self.book) == self.cap:
                las = self.last.pre
                las.pre.nex = las.nex
                las.nex.pre = las.pre
                las.pre, las.nex = None, None
                del self.book[las.key]
            self.book[key] = node
        self._to_top(node)
        
    # put a dll node or new node to top (nex of dummy)
    def _to_top(self, node:Node) -> None:
        if node.pre == self.dummy:
            return
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
        cur_head = self.dummy.nex
        node.pre, node.nex = self.dummy, cur_head
        cur_head.pre, self.dummy.nex = node, node

