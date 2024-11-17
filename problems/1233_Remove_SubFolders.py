'''
Leetcode 1233. Remove Sub-Folders from the Filesystem
Given a list of folders, remove the path that is a sub folder of some other path in the list.

Build a dict of dict as Trie. parent: dict(sub folder)
If a path reaches its end in the Trie, record its idx in list.
If the Trie gives idx value instead of dict while traversing a path,
	stop early because an ancestor path was seen earlier.

Then recursively unpack the Trie by collecting idx.
Reconstructing path string from the Trie keys also works.
'''
from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Trie by dict
        book = {}
        for idx, foo in enumerate(folder):
            pre, cur = None, book
            # regex also works, but a bit slow for this simple match
            path = foo[1:].split('/')
            path.append('')
            # record idx of each common parent path for quicker reference later
            for f in path:
                # this path ends, thus record its idx
                if not f:
                    pre[path[-2]] = idx
                    break
                # create subtrie
                if f not in cur:
                    cur[f] = {}
                # some previous path ends here, then no need to continue on this path
                elif type(cur[f]) is int:
                    break
                pre, cur = cur, cur[f]

        # recursively collect existing paths in book
        res = []
        def recur(d: dict) -> None:
            for v in d.values():
                if type(v) is int:
                    res.append(v)
                else:
                    recur(v)
        recur(book)
        return [folder[t] for t in res]