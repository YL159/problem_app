'''
Leetcode 2434. Using a Robot to Print the Lexicographically Smallest String
Given string s, a robot can:
	consume and store a left char from s in its internal stack
	write its stack-top letter to paper
Find the lexicographically smallest string on paper.

Try to write all instance of current smallest letter as front as possible
	=>	as long as there are such letters in s, we can consume and print them as front as possible
    =>	print stack-top letters that is no greater than current smallest letter

e.g. s = "vzhofnpo", letter lexico: f, h, n, o, p, v, z. Strategy is to check letters from small to great.
for f: can make sure it is printed first, but now next smallest letter h is in stack [v,z,h,o]
for h: no further h in remaining 'npo'.
	Here we can't turn back and force print out h in stack:
    If some h are accessible on top of stack, sure we can print them
    	=> print any stack-top letter no greater than h is acceptible
        beyond them will be greater letters not necessarily next to h
    Stack-top is o > h, stop printing from stack
for n: 1 left in 'npo', consume and pring immediately
for o: 1 left in 'po' and 1 left at stack top:
	print stack-top smaller letters first, to make sure letters <= o are printed
    then consume and print o in string s, because there are only greater letters entering stack
		because all of smaller letters were consumed in previous iterations
then deal with pvz.
Time O(n+26*log26) = O(n), Space O(n)
'''
import collections

class Solution:
    def robotWithString(self, s: str) -> str:
        book = collections.Counter(s)
        i = 0
        stack, res = [], []
        for c in sorted(book.keys()):
            if not book[c] and (not stack or stack[-1] != c):
                continue
            # clear stack top letters <= c
            while stack and stack[-1] <= c:
                res.append(stack.pop())
            # put remaining c in s all to paper
            while book[c] and i < len(s):
                if s[i] == c:
                    res.append(s[i])
                else:
                    stack.append(s[i])
                book[s[i]] -= 1
                i += 1
        # put remaining char in stack to paper
        while stack:
            res.append(stack.pop())
        return ''.join(res)
            