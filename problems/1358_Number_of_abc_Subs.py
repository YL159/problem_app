'''
leetcode 1358. Number of Substrings Containing All Three Characters
Find the number of substrings containing a, b, c

Use matrix and index reference to keep track of current triplet of tight abc substring
And count its right options. Left option is always 1 because s contains only abc letters.
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # similar to #930, use altered sliding window
        # get the list of indices of abc respectively for easier jumping
        ref = {'a':0, 'b':1, 'c':2}
        abc = [[], [], []]
        for i in range(len(s)):
            # s has only a, b, c
            abc[ref[s[i]]].append(i)
        if not abc[0] or not abc[1] or not abc[2]:
            return 0
        cur = {0:0, 1:0, 2:0}
        last = min(abc[0][-1], abc[1][-1], abc[2][-1])
        start, res = 0, 0
        while start <= last:
            end = max(abc[0][cur[0]], abc[1][cur[1]], abc[2][cur[2]])
            # left is always 1
            # right has choices till the end of s
            res += len(s) - end
            cur[ref[s[start]]] += 1
            start += 1
        return res
    
# another great solution:
# this at core is similar to my solution, but looking back to start of s
# my solution looks to the end of s. So either loop backwards and use the following with max
# Or keep track of valid ends of substrings

# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         d = {}
#         n = len(s)
#         total = 0
#         for i in range(n):
#             d[s[i]] = i
#             if len(d) == 3:
#                 min_loc = min(d.values())
#                 total += min_loc + 1

#         return total