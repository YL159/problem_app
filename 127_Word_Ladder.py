from typing import List
'''
Leetcode 127. Word Ladder
n - length of wordList, m - length of beginWord
The majority of solutions use partial string matching (or regex-like grouping):
time complexity O(nm^2) if omitting nested alphabet loops

This solution approach differently by grouping the wordList words into m different buckets/layers,
using the count of positional letter difference from endword.
And in the word graph, neighboring word edge can only come from within the same distance layer or neighboring layers.
Then use BFS from the graph centered by the endWord to find the path length to beginWord

This solution is not a time efficient solution.
If the wordList's words are randomly chosen, then each distance layer contains O((mk)^t) words
where k is the char set size, t is the layer number, i.e. t different positional letters from endWord.
And the series add up to wordList length n

With some calculation, my solution has time complexity of O(n^2)
While the wordList length n is far larger than word length m, this solution is not time efficient.
'''
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    def distance(w1: str, w2: str) -> int:
        count=0
        for i in range(len(w1)):
            count += w1[i] != w2[i]
        return count

    # first construct word distance layers from endWord
    dis_map={x: set() for x in range(len(beginWord)+1)}
    for w in wordList:
        dis_map[distance(endWord, w)].add(w)

    # construct adjacency map from dist_map
    # O(n^2/m) to find every edge, by only checking same and next neighbor layer
    adj_map={}
    for i in range(len(beginWord)+1):
        level = dis_map[i].copy()
        for w1 in dis_map[i]:
            level.remove(w1)
            nex = dis_map.get(i+1, set())
            # same & next level neighbor
            for w2 in level.union(nex):
                if distance(w1, w2) == 1:
                    if w1 in adj_map:
                        adj_map[w1].add(w2)
                    else:
                        adj_map[w1] = set([w2])
                    if w2 in adj_map:
                        adj_map[w2].add(w1)
                    else:
                        adj_map[w2] = set([w1])


    # then start from endWord, BFS till a word within 1 neighbor from beginWord, record layer number
    res = 1
    layer = set([endWord])
    visited = set([endWord])
    while layer:
        tmp = set()
        for w in layer:
            if distance(beginWord, w) == 1:
                return res + 1
            tmp = tmp.union(adj_map.get(w, set()).difference(visited))
        visited = visited.union(layer)
        layer = tmp.difference(visited)
        res += 1
    return 0
