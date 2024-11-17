'''
Leetcode 433. Minimum Genetic Mutation
Given startGene, endGene and gene bank, find the shortest mutation path from start to end.
Each node in path should be in the bank, except for start. Mutation takes 1 place at a time.

Use topoligical sort from the start gene on the gene bank. It is BFS and guarantees shortest path.
'''
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        res = 0
        cur = {startGene}
        # gene graph bfs/topoligical sort. A gene may have multiple parents.
        # but search depth 'res' is min
        while endGene not in cur and bank and cur:
            res += 1
            nex = set()
            for cur_gene in cur:
                for gene in bank:
                    if self.diff1(gene, cur_gene):
                        nex.add(gene)
            bank -= nex
            cur = nex
        if endGene not in cur:
            return -1
        return res
    
    # check if 2 genes differ exactly 1 position
    def diff1(self, g1: str, g2: str) -> bool:
        chance = True
        for i in range(len(g1)):
            if g1[i] != g2[i]:
                if not chance:
                    return False
                chance = False
        return chance == False
        