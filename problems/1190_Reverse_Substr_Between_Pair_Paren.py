'''
Leetcode 1190. Reverse Substrings Between Each Pair of Parentheses
Given a string with valid parentheses, expand parentheses by reversing each pair's content.

Use stack to record the current depth and buffered chars of the same depth
Eventually make stack[0] looks the same as the given string s if printed out.
Then recursively expand the result nested list.

Ideally it is O(n) time
since we reverse odd layer's chars and deeper list refs, instead of all chars on & below this depth
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur = []
        stack.append(cur)
        # make a nested list of char/list
        for c in s:
            if c == '(':
                # halt & stack current list, and make cur point to new []
                cur.append([])
                stack.append(cur)
                cur = cur[-1]
            elif c == ')':
                # stack starts with len=1
                # thus even len of stack => odd paren depth
                if len(stack) % 2 == 0:
                    cur.reverse()
                cur = stack.pop()
            else:
                cur.append(c)
        # print(stack)
        self.res = []
        self.expand(stack[0])
        return ''.join(self.res)
    
    def expand(self, nested: list) -> None:
        for x in nested:
            if type(x) is str:
                self.res.append(x)
            else:
                self.expand(x)
    
