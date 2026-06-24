'''
Leetcode 60. Permutation Sequence
Permutations of [1, 2, 3...n] digits are sorted in lexico order.
    n = 3: 123, 132, 213, 231, 312, 321
Find kth permutation string, 1-indexed.

Observation:
Permutation count of n digits are of n! order
    => generating them and sort to find kth is not feasible
Consider most significant digit 1 and 2, their tail combination counts are the same
    => use tail comb count modulo to skip chunks of k
    => reduce tail comb on the fly

Calculate the tail combination count each round, get k's quotient and remainder of comb
    => quotient tells the index of digit to take from available digits
    => remainder is k of the next iteration, reduce comb accordingly

Time is roughly O(n^2)
1. n^2 for taking digits in order
2. k is of n! scale, yet also divided by a shrinking comb factor based on n
    => thus iteration count is still O(n), even though k is the loop variable
Space O(n)
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # decide digit from most significant to least significant
        if n == 1:
            return "1"
        
        candidates = [str(i) for i in range(1, n+1)]

        comb = 1
        for i in range(2, n):
            comb *= i
        tail = n-1
        k -= 1  # accommodate 1-index
        digits = []
        
        while k > 0:
            idx = k // comb
            k %= comb
            digits.append(candidates[idx])
            del candidates[idx]

            comb //= tail
            tail -= 1
        
        digits.extend(candidates)
        return ''.join(digits)