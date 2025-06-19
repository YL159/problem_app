'''
Leetcode 440. K-th Smallest in Lexicographical Order
Similar to #386, but just find the kth number in lexico ordered int array.

Method 1, enumerate each number as in #386 for the kth smallest. Time O(k), Space O(logk)

Methdo 2, skip some subtrees and go into interested subtree
In order to quickly locate target position, we should skip unnecessary subtrees
	=> need to use time < O(n) to determine subtree size
Notice that for each subtree, it is either complete or incomplete
	Complete subtree size: 1+10+100+... = 11...1
	Incomplete subtree size: all tree size - sum(complete subtree size)

e.g. for n = 25, initial subtree sizes: [0, 11, 7, 1, 1, 1, 1, 1, 1, 1]
			trie root (prefix)			 0	1	2  3  4  5  6  7  8  9
left complete subtree size = 11, right complete size = 1, incomplete = 25 - 11 - 1*7 = 7
O(1) time to find subtree size

If go into subtree(1), subtree of complete subtree is still complete, left = right = 1.
If go into subtree(2), left = 11//10 = 1, right = 1//10 = 0.
Whenever go into a subtree, append trie root to result
Time O(logk), Space O(1)

Method 3, from solutions, recursively determine each subtree's size and skip
Similar idea as method 2, but dynamically determine each subtree's size by using next subtree's same level info
Time O(logn*logk), since each time we go into a subtree by levels. Space O(1) if not considering call stack.
'''
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # method 2, inspired by discussion
        # 1st digit < 1st(n) has full tree of 111...1 len(n) 1s
        # > 1st(n) has full tree of len(n)-1 1s
        ns = [int(d) for d in str(n)]	# make digit list of n
        i = 0	# ns digit index
        total = n	# count of numbers in current trie, initially all n
        left = int('1'*len(ns))	# full subtree size before some incomplete subtree, 11..1
        right = left // 10	# full subtree size after the incomplete subtree, 1..1 one less 1s
        res = 0
        
        while k > 0:
            # quickly generate size of all subtrees in current level
            subtree = [0] * 10
            for d in range(10):
                if i == 0 and d == 0:
                    continue
                if d < ns[i]:
                    subtree[d] = left
                elif d > ns[i]:
                    subtree[d] = right
            subtree[ns[i]] = total - sum(subtree)
            # skip some subtrees if its size smaller than remaining count k
            for d in range(10):
                if k > subtree[d]:
                    k -= subtree[d]
                    continue
                res *= 10
                res += d
                total = subtree[d] - 1
                k -= 1
                break
			# update ns index and left/right subtree count
            # if going into a complete subtree, left & right will be the same and still be complete, i will be useless
            # if going into incomplete subtree, i will still be useful, left/right remain different and reduce
            i += 1
            if total == left - 1:
                right = left
            elif total == right - 1:
                left = right
            left //= 10
            right //= 10

        return res