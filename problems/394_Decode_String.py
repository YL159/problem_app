'''
leetcode 394. Decode String

Recursively resolve inner [] and combine
'''

class Solution:
    def decodeString(self, s: str) -> str:
        # recursive solution
        if '[' not in s:
            return s
        stack, buff, num = [], [], []
        start, end, n = 0, 0, 0
        for i, c in enumerate(s):
            if c.isnumeric():
                if not stack:
                    num.append(c)
            elif c == '[':
                if not stack:
                    start = i + 1
                stack.append(c)
            elif c.isalpha():
                if not stack:
                    buff.append(c)
            else: # ']'
                stack.pop()
                if not stack:
                    end = i
                    n = int(''.join(num))
                    buff.append(self.decodeString(s[start:end]) * n)
                    num = []
        return ''.join(buff)