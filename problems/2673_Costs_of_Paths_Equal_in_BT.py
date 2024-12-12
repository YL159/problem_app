'''
Leetcode 2673. Make Costs of Paths Equal in a Binary Tree
For a perfect BT of n nodes, label 1-n. And a cost arr for each node.
An op: choose 1 node lift its cost by 1
Find the min # of op that makes all path from root to leaf the same.

To get min op, try to make each path cost equal to max path cost
Increase inner node is more favorable than increasing leaf node, cust inner node affects more paths.
But inner node can only increase to a limit where a max path crossing it reaches global max.
Then iterate its children of lesser path cost.

Method 1:
Find global max path cost, and store the max path cost from each node to leaf.
This helps determing the max increase for each node later.
Then use pre order traversal, to make each node's max path match target path cost.
Time O(n), space O(n)

Method 2:
While working with pre order, each node's lift = target - max path cost of node
thus for children nodes, new target = target - node's lift - node's cost = max path cost of node - node's cost
as if for each node, the target is not quite dependent on the pre-calculated global max path cost
=> for each node, its lift depends on its sibling. Always lift both siblings to the max of them.
And use given list of cost to both node cost & keep track of the current node's max path down to leaf.
Time O(n), space O(1)
'''
from typing import List

class Solution:
    # method 1
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # min op => each op affects as many as possible insuff paths
        self.leaf0 = (n+1)//2
        self.cost = cost
        self.nodes = [0] * n
        great = self.postOrder(1)
        self.res = 0
        self.preOrder(1, great)
        return self.res

    # post order find max path sum, and max path sum from leaf to each node
    def postOrder(self, rt: int) -> int:
        if rt >= self.leaf0:
            self.nodes[rt-1] = self.cost[rt-1]
            return self.cost[rt-1]
        mx_sum = max(self.postOrder(rt*2), self.postOrder(rt*2+1)) + self.cost[rt-1]
        self.nodes[rt-1] = mx_sum
        return mx_sum

    # pre order check diff(node's max sum, target), add to op #
    # smaller subtree path can just align with its greater sibling sum
    def preOrder(self, rt: int, target: int) -> None:
        self.res += target - self.nodes[rt-1]
        if rt >= self.leaf0:
            return
        diff = self.nodes[rt-1] - self.cost[rt-1]
        self.preOrder(rt*2, diff)
        self.preOrder(rt*2 + 1, diff)
    
	# # method 2
    # def minIncrements(self, n: int, cost: List[int]) -> int:
    #     res = 0
    #     for node in range(n//2, 0, -1):
    #         l, r = cost[node*2-1], cost[node*2]
    #         # align left & right path sums
    #         res += abs(l - r)
    #         # update cur root's max path sum to leaf
    #         cost[node-1] = max(l, r) + cost[node-1]
    #     return res