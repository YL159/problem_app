import collections
'''
76. Minimum Window Substring
Theorem: each min substr containing t, has both sub[0], sub[-1] frequencies in substr equal to their frequencies in t.
Find initial substring, r moves till another l letter, then l moves till l's letter gets the same letter frequency in t
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        target = collections.Counter(t)
        source = collections.Counter(s)
        for k, v in target.items():
            if k not in source or source[k] < v:
                return ''
        # finding initial l, r position from 0, len(s)-1
        l, r = 0, len(s)-1
        while r > l:
            if s[r] in target:
                if source[s[r]] > target[s[r]]:
                    source[s[r]] -= 1
                else:
                    break
            r -= 1
        while l < r:
            if s[l] in target:
                if source[s[l]] > target[s[l]]:
                    source[s[l]] -= 1
                else:
                    break
            l += 1
        # move r pointer while l pointer letter more than target
        res = (l, r+1)
        opt = r-l+1
        r += 1
        while r < len(s):
            if s[r] != s[l]:
                if s[r] in target:
                    source[s[r]] += 1
                r += 1
                continue
            source[s[l]] += 1
            # move l till some letter counts the same as target
            # same as finding initial l
            while l < r:
                if s[l] in target:
                    if source[s[l]] > target[s[l]]:
                        source[s[l]] -= 1
                    else:
                        break
                l += 1
            if r-l+1 < opt:
                res = (l, r+1)
                opt = r-l+1
            r += 1
        return s[res[0]:res[1]]