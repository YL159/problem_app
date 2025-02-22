'''
1415. The k-th Lexicographical String of All Happy Strings of Length n
Sort in lex order of all Happy strings of length n:
1. Use only 'abc'.
2. No 2 neighbor letters are the same.
Return kth string of this string list.

For some string '...acb', the next letter's choice is among {a, b, c} - {string[-1]}, 2 choices
Except the 1st letter has 3 choices.
=> The happy strings forms 3x binary trees, and k determines the path from root to target leaf
Time O(n), space O(n)

Follow up: Happy string use m chars.
Then the str space is mx (m-1)-ary trees.
'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # total str count 3*2^(n-1)
        # k determines happy str tree path
        total = 3*2**(n-1)
        if k > total:
            return ''
        t3 = total // 3
        res = []
        # memo 'other' set choices, 3 of them. and ordered
        letters = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}
        
        def traverse(left: int, right: int, other: list) -> None:
            if len(res) == n:
                return
            mid = (left + right) // 2
            if k <= mid:
                res.append(other[0])
                traverse(left, mid, letters[res[-1]])
            else:
                res.append(other[1])
                traverse(mid, right, letters[res[-1]])
            
        if 0 < k <= t3:
            res.append('a')
            traverse(0, t3, letters['a'])
        elif t3 < k <= 2*t3:
            res.append('b')
            traverse(t3, 2*t3, letters['b'])
        else:
            res.append('c')
            traverse(2*t3, total, letters['c'])
        return ''.join(res)