'''
Leetcode 1930. Unique Length-3 Palindromic Subsequences
Count all unique length-3 aba-like subsequences of a string

# Method 1
Find the start and end indices of each letter (max 26), start letter will be unique for each range.
Get the set of letters between each pair of [start, end] and count

Time: O(n). Worst case traverse the string s 26 times, because of finding set of letters between two idx
Space: O(1). Collect only 26 letter related info


# Method 2
Similar to method 1, but use prefix letter counter snapshot for quick checking letters in between.
1. get the 1st/last appearance for each letter
2. collect max 26*2 point(idx) of interests for the letters
3. snapshot prefix letter count for these interested idx => important for O(1) space use
4. for each letter, check prefix letter count difference, count if any remains.
Same Time and Space as method 1, but traverse s only twice instead of 26 times max
'''

class Solution:
    # method 1
    def countPalindromicSubsequence(self, s: str) -> int:
        # { letter: [start, end] } end=-1 means letter appear only once
        book = {}
        for i, c in enumerate(s):
            if c not in book:
                book[c] = [i, -1]
            else:
                book[c][1] = i
        # get the set of letters between each palindrome starter, O(26*n)
        book1 = {k:set() for k in book}
        for k, [start, end] in book.items():
            if end > 0:
                book1[k] = set(s[start+1:end])

        count = sum([len(v) for v in book1.values()])
        return count
    

    # # method 2
    # def countPalindromicSubsequence(self, s: str) -> int:
    #     a = ord('a')
    #     abc = [chr(a+i) for i in range(26)]
    #     # 1. { letter: [start, end] } end=-1 means letter appear only once, time n
    #     book = {}
    #     for i, c in enumerate(s):
    #         if c not in book:
    #             book[c] = [i, -1]
    #         else:
    #             book[c][1] = i
    #     # 2. collect crutial points (max 2) for each abc letter, time 2*26 
    #     points = set()
    #     m = 0
    #     for c, v in book.items():
    #         if v[1] == -1:
    #             continue
    #         points.update(v)
    #         m = max(m, v[1])
    #     # 3. snapshot letter counts for each interested points, time n ~ n+52*26
    #     record = {}
    #     count = collections.defaultdict(int)
    #     for i, c in enumerate(s):
    #         count[c] += 1
    #         if i in points:
    #             record[i] = [count[x] for x in abc]
    #         if i == m:
    #             break
    #     # 4. for each start letter, find # of different letters between. time 26*26
    #     res = 0
    #     for c, [start, end] in book.items():
    #         if end == -1:
    #             continue
    #         for i, [x, y] in enumerate(zip(record[start], record[end])):
    #             remain = y - x - (abc[i] == c)
    #             res += remain > 0
    #     return res