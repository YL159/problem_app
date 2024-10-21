'''
Leetcode 3. Longest Substring Without Repeating Characters
Find its length

Use sliding window, and a hashmap to record latest position of each char.
When current char appears in hashmap and its latest position is within the window, time to record this substr
Also wrap up the last char position
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # update on sliding window
        if len(s) <= 1:
            return len(s)
        book = {}
        res, l = 0, 0
        for i, c in enumerate(s):
            # record current substr len
            if c in book and book[c] >= l:
                res = max(res, i - l)
                # book[c] is guaranteed the latest position of c
                l = book[c] + 1
            # update each char latest position
            book[c] = i
        res = max(res, i + 1 - l)
        return res

		# Earlier version, traverse twice is not necessary
        # sliding window, record the max of every non-repeating substring
        # n = len(s)
        # if n < 2:
        #     return n
        # l, r = 0, 1
        # book = {s[l]: l}
        # res = 1
        # while r < n:
        #     cur=s[r]
        #     if book.get(cur, -1) >= 0:
        #         res = max(res, r-l)
        #         index = book[cur]
        #         while l <= index:
        #             book[s[l]] = -1
        #             l += 1
        #     book[cur] = r
        #     r += 1
        # if s[r-1] in book:
        #     res = max(res, r-l)
        # return res
        