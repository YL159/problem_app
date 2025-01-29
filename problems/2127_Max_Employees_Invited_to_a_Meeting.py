'''
Leetcode 2127. Maximum Employees to Be Invited to a Meeting
N employees each has a favorite other employee. Employee i favors employee favorite[i].
Company wants to invite some employees to a meeting with following conditions:
1. The only round table can seat as many employees as possible.
2. Only when employee i's favorite other employee is invited, he/she will accept invitation.
3. At the table, each employee will sit next to his/her favorite other employee.
Find the max # of employees to successfully invited and be seated.

We can make the following observations and deductions:
1. The employees form a directed graph.
2. Since employee can't favor him/herself, there is no stand-alone favorite chain.
	=> All favorite chain ends with a loop somewhere.
3. For members in a loop, none will accept invitation unless all of them are invited.
    From 2, branches favor towards a loop, not the reverse.
	Thus inviting branches(chains) attached to some loop depends on inviting the whole loop first.

4. Deduct from 2 & 3: No 2 loops share an edge, a member or a branch member.
	a) Each loop is directed (anti)clockwise. Otherwise a member in a loop will favor 2+ people.
	b) If 2 loops share an edge or a member, since a), there will be a loop member favor 2+ people.
    c) If 2 loops share a branch, it contradicts to 3's "branches favor towards 1 loop".
5. Deduct from 1 & 4: Each loop belongs to, and represents one connected component in the graph.
	There are branches connects to some loop members, and there may be branches of branches.

6. We can invite as many 2-member loops/circles as possible, or only one loop/circle of 3+ members.
	For 3+ circle, each member i's 2 neighbors at the table will be occupied by 2 different employees:
		i's fav AND the one fav i
    For 2-circle, each member i has 1 extra space for i's potential branch.

7. Deduct from 5 & 6:
	Either invite all 2-member loops, with 1 longest branch available for each member.
    Or invite 1 of the longest 3+ circles, with no branches at all.

Solution: check the code comments.
Use DFS on each employee, build it's path to a loop or loop itself.
Whenver encounters a visited node, prune the traversal by:
	If a 2-circle node, update branch node's distance to the circle entrance node.
    If a branch node leading to a 2-circle, update branch's new node's distance to the circle using recorded branch node distance.
		and update circle entrance node's longest branch length.
    If a 3+ circle node or branch node leading to a 3+ circle, ignore the branch since they are not involved in getting results.
If all nodes unvisited, it eventually encounter a node appeared in the path/chain, indicating a new loop found.
	If loop is 2-circle, initiate circle nodes' longest branch count.
    If loop is 3+ circle, update the history 3+ circle max length.
Thus each node in the graph is visited exactly once.
'''
from typing import List
import collections

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # can take as many 2-circle as possible, with max branches
        # or take one largest >= 3 circle, with no any branches
        
        # a 2-circle node: max chain length from some chain node to it
        two_chain = collections.defaultdict(int)
        # a node ends at some 2-circle node: [target 2-circle node, distance]
        chain_nodes = collections.defaultdict(list)
        # nodes belong to a 3+ circle
        circles = set()
        # longest 3+ circle
        self.three_more = 0
        visited = set()

        def dfs(node: int) -> None:
            chain = [node]
            chain_pos = {node: 0}
            fav = favorite[node]
            while fav not in chain_pos:
                # early exit if fav is a 2-circle node
                # or visited chain node ends at a 2-circle node
                if fav in chain_nodes:
                    target, d0 = chain_nodes[fav]
                    for i, n in enumerate(chain):
                        chain_nodes[n] = [target, len(chain)-i+d0]
                    two_chain[target] = max(two_chain[target], len(chain)+d0)
                    visited.update(chain)
                    return
                # early exit if fav is in 3+ circle
                # or some other visited node, such as chain node ends at a 3+ circle node
                if fav in circles or fav in visited:
                    visited.update(chain)
                    return
                # otherwise extend current chain untill loop detected
                chain_pos[fav] = len(chain)
                chain.append(fav)
                fav = favorite[fav]
            start = chain_pos[fav]
            # deal with 2-circle and its chains
            if len(chain) - start == 2:
                for i, n in enumerate(chain[:-1]):
                    chain_nodes[n] = [chain[start], len(chain)-i-2]
                chain_nodes[chain[-1]] = [chain[-1], 0]
                two_chain[chain[start]] = len(chain) - 2
                two_chain[chain[-1]] = 0
            # deal with 3+ circle, only update max circle length
            else:
                self.three_more = max(self.three_more, len(chain) - start)
                circles.update(chain[start:])
            visited.update(chain)

        for i in range(len(favorite)):
            if i in visited:
                continue
            dfs(i)
        # the table can take all 2-circles and their longest chains if any
        all_twos = sum(v+1 for v in two_chain.values())
        # or just take the largest 3+ circle without any chains
        return max(all_twos, self.three_more)

