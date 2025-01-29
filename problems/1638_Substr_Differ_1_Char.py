'''
Leetcode 1638. Count Substrings That Differ by One Character
Given string s and t, find # of ways to choose some non-empty substr s and t:
    substr are of equal length
    differ by exactly 1 char

e.g. s: ways, t: await
We want to align them in as many ways as possible to find all diff-1 substr
ways|       ways|       ways|      |ways|  |ways|   |ways ...
  |await     |await     |await     |await  await|  await| ...
We can focus on the range they meet, and mark their match/diff positions using matrix instead:
  a w a i t
w 0 1 0 0 0     Each diagonal array in the matrix: char match when s&t aligned at some position
a 1 0 1 0 0
y 0 0 0 0 0
s 0 0 0 0 0
          | diagonal array -> |ways|wait| -> [1,1,0,0]
Since we allow 1 char diff for substr, see each diff char (indicator 0) as center:
    count how many same char extends to its left/right
    => count of valid substr = same char left * same char right
    same char default is 1, allowing 1 * n = n, meaning that side has no same char
Thus above diff array |ways|wait| -> [1,1, 0, 0 ] generates same char count around each diff char:
                                          3, 1, 1
    then sum(pairwise mult), 3*1 + 1*1 = 4 is the count of target substr pairs:
        3:'way'-'wai', 'ay'-'ai', 'y'-'i';
        1:'s'-'t'
    deduction is time O(len(diagonal))

Since we travers the above matrix's each diagonal array once, time complexity is O(m*n), space O(m*n)
'''
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        # traverse a diagonal arr of s-t letter difference matrix
        def diagonal(tot: int, i: int) -> int:
            j = tot - i
            # inter records the choice between neighbor mismatch
            # min 1 for no letter, i.e. diff letter at substr edge
            inter = []
            count = 1
            while i >= 0 and j >= 0:
                if t[i] == s[j]:
                    count += 1
                else:
                    inter.append(count)
                    count = 1
                i -= 1
                j -= 1
            inter.append(count)
            res = 0
            for k in range(len(inter)-1):
                res += inter[k] * inter[k+1]
            return res
        
        result = 0
        for total in range(m-1, m+n-1):
            result += diagonal(total, m-1)
        for total in range(m+n-3, n-2, -1):
            result += diagonal(total, total-n+1)
        return result