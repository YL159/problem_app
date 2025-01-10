'''
Leetcode 2484. Count Palindromic Subsequences
Count the number of all palindromic subseq of length 5 in string s. s has only number chars.
Same palindroms with different idx combinations count as different.

00-99 there are 100 kinds of prefix 2 number for such palindrom.
For each possible 'middle' position, we want to know how many, say for prefix '12' on its left
	and how many '21' on its right.
    => Add their product to result, cus the anchor 'middle' is different from other future 'middles'
Consider 112[2]321 working at [2] now. Its left '12' pair got 2x, right '21' got 1x
	=> 1122[3]21 working at [3] now. The new 2 added to the left, creating 2x more '12' because of 2x '1'
This means we should also keep track of number counts, in order to update pair counts

Working from idx 2 to last possible idx, collect results and update left/right number count and pair counts.
Time O(n) worst case 100*(n-2), space O(1), 200
'''
class Solution:
    def countPalindromes(self, s: str) -> int:
        if len(s) < 5:
            return 0
        # keep track of how many 'xy' to the left of mid, and 'yx' to the right
        left, leftp = {s[0]:1}, {s[:2]: 1}
        left[s[1]] = left.get(s[1], 0) + 1
        right, rightp = {s[-1]:1}, {s[-2:]: 1}
        right[s[-2]] = right.get(s[-2], 0) + 1
        for i in range(len(s)-3, 2, -1):
            for k, v in right.items():
                t = s[i]+k
                rightp[t] = rightp.get(t, 0) + v
            right[s[i]] = right.get(s[i], 0) + 1
        # iterate on each mid char, mult the matching left/right pairs
        res = 0
        for i in range(2, len(s)-2):
            for t in leftp:
                tr = t[1] + t[0]
                res += leftp[t] * rightp.get(tr, 0)
            # update left/leftp
            for k, v in left.items():
                t = k + s[i]
                leftp[t] = leftp.get(t, 0) + v
            left[s[i]] = left.get(s[i], 0) + 1
            # update right/rightp
            nex = s[i+1]
            right[nex] -= 1
            if right[nex] == 0:
                del right[nex]
            for k, v in right.items():
                tr = nex + k
                rightp[tr] -= v
        return res % (10**9+7)