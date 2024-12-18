'''
Leetcode 264. Ugly Number II
Give nth number from 1 that contains only 2,3 or 5 as factors.
1,2,3,4,5,6,8,9,10,12...

My solution on Leetcode
https://leetcode.com/problems/ugly-number-ii/solutions/6150582/3-ordered-deques-with-min-on-by-longinus-g8bv/

Idea is to maintain 3 sorted list of multiple of 2/3/5.
We can prove that with precedence (e.g 2->3->5) multiplication and only appending new items:
	the lists are sorted
    every target number is generated, and only once

[2], [3], [5] => pop 2, follow precedence, mult 2,3,5 and get 4,6,10, assign (append) them to corresponding lists.
[4], [3,6], [5,10] => pop 3, follow precedence, mult 3,5 and get 9,15, append to corresponding lists.
[4], [6,9], [5,10,15] still ordered. Pop 4
[8], [6,9,12], [5,10,15,20] still ordered.
etc.

Time complexity O(n)
Space complexity seemingly O(n), the following tests show that space demand growth is slower than n's growth
'''
import collections

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # maintain 3 ordered deque, q2, q3, q5.
        # num popped from q2 mult 2,3,5 and append to corresponding que
        # num popped from q3 mult 3,5
        # num popped from q5 mult only 5
        # appending operation maintains deque's increasing order
        if n == 1:
            return 1
        q2, q3, q5 = 2, collections.deque([3]), collections.deque([5])
        res = 2
        m = 0
        for i in range(n-1):
            res = min(q2, q3[0], q5[0])
            if res == q2:
                q2 *= 2
            if res == q3[0]:
                q3.popleft()
            if res == q5[0]:
                q5.popleft()
            else:
                q3.append(res * 3)
            q5.append(res * 5)
            m = max(len(q3) + len(q5), m)
        print(n, m, f'{n/m = :.2f}')
        return res

if __name__ == '__main__':
    sol = Solution()
    for i in range(1000, 2000, 100):
    	sol.nthUglyNumber(i)
    