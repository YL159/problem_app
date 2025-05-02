'''
Leetcode 838. Push Dominoes
Give some L/R force to some dominoes in an array of initially standing dominoes,
each second the affected standing domino will fall to pushed direction,
a domino affected by L and R at the same time will remain standing.
Find the final L/R state of the dominoes.

Method 1, state machine and check each dominoes considering prev R
Time O(n), Space O(1)

Method 2, scan L only for 1st pass, mark standing dominoes with (L, time) marking when it will fall to L
2nd pass resolve R, march standing dominoes and check which of L/R arrive early.
Time O(n), Space O(n)
'''
class Solution:
    # method 2, modularized L/R sweep and combine
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        # initialize with larger time for easier comparison, instead of None or -1
        times = [[n, n] for _ in range(n)]

        # process L and R separately, find domino state change time
        def sweep(letter: str) -> None:
            reverse = letter == 'L'
            idx = 0 if reverse else 1
            state, t = None, 0
            for i in range(n):
                if reverse:
                    i = n-1-i
                if dominoes[i] == '.':
                    if state == letter:
                        t += 1
                        times[i][idx] = t
                elif dominoes[i] == letter:
                    state, t = letter, 0
                    times[i][idx] = 0
                elif state == letter:
                    state = None

        sweep('L')
        sweep('R')
        res = []
        for a, b in times:
            if a < b:
                res.append('L')
            elif a > b:
                res.append('R')
            else:
                res.append('.')
        return ''.join(res)

    # # Method 1, state machine
    # def pushDominoes(self, dominoes: str) -> str:
    #     gotR = False
    #     dots = 0
    #     res = []
    #     for i, d in enumerate(dominoes):
    #         # resolve L
    #         if d == 'L':
    #             if not gotR:
    #                 res.append('L'*dots)
    #             else:
    #                 gotR = False
    #                 res.append('R'*(dots//2))
    #                 if dots % 2:
    #                     res.append('.')
    #                 res.append('L'*(dots//2))
    #             res.append('L')
    #             dots = 0
    #         # resolve R
    #         elif d == 'R':
    #             if not gotR:
    #                 gotR = True
    #                 res.append('.'*dots)
    #             else:
    #                 res.append('R'*dots)
    #             res.append('R')
    #             dots = 0
    #         # count .
    #         else:
    #             dots += 1
    #     # resolve remaining .
    #     if dots:
    #         c = '.' if not gotR else 'R'
    #         res.append(c*dots)
    #     return ''.join(res)