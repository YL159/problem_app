'''
Leetcode 1079. Letter Tile Possibilities
Given a series of letter tiles, find ways to arrange them. From 1 to all tiles

There are 26 different tiles. Arrangements are different if letters are different at some idx.
Thus we can fix each position with different letters, by back tracking in recursive calls:
For ABCDD -> A.... -> A
				   -> AB... -> ...
		  		   -> AC... -> ...
				   -> AD... -> ...
		  -> B.... -> BA... -> ...
		  ...
Find the possibilities/arrangements of remaining letter tiles
And add all of them up, because each leaf is unique.

But in the process we can improve by caching calculated results:
For AABBC, fix AB... finding combinations of remaining ABC, is the same as fixing BA... finding remaining ABC
Thus we cache calculated ABC combination count in 'record' as 'A1B1C1' : 15.

The representation of remaining tiles should be sorted, because 'A1B1C1' is the same as 'B1A1C1'
Thus to reduce cache size and avoid repeatitive calculation.
'''
import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        book = collections.Counter(tiles)
        # cache/DP already solved sub problems, by ordered letter:freq sequence
        self.record = {f'{k}1': 1 for k in book}
        self.DFS(book)
        return sum(self.record.values())

    def DFS(self, book: dict) -> int:
        # make an ordered string representation of current remaining tiles
        ref = [f'{k}{v}' for k, v in book.items() if v != 0] 
        rep = ''.join(sorted(ref))
        if rep in self.record:
            return self.record[rep]
		# back tracking DFS on a new set of remaining tiles
        res = 0
        for k, v in book.items():
            if v == 0:
                continue
            book[k] -= 1
            res += self.DFS(book)
            book[k] += 1
        
        self.record[rep] = res
        return res

        