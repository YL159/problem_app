'''
LeetCode 721 Accounts Merge
union find.
'''
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # collect serial:name and serial:emails
        name_book = {}  # serial : name
        email_book = {} # serial : email_set
        email_ref = {}    # email : serial_set
        connection = {i:{i} for i in range(len(accounts))}  # serial : serial_set
        for n, lis in enumerate(accounts):
            name_book[n] = lis[0]
            email_book[n] = set(lis[1:])
            # collect the email:presence reference map
            for email in email_book[n]:
                if email not in email_ref:
                    # email 1st met, points to earlist account serial #
                    email_ref[email] = [n]
                else:
                    # reappearance will update graph connection map
                    last = email_ref[email][-1]
                    connection[last].add(n)
                    connection[n].add(last)
                    email_ref[email].append(n)

        # union the graph nodes into groups
        result = []
        check = set()
        for n, lis in connection.items():
            # skip already visited account node
            if n in check:
                continue
            res = [name_book[n]]
            # nodes with connection means union find, using BFS
            prev, cur = lis, lis.copy()
            added = lis.copy()
            while added:
                check = check.union(added)
                for i in added:
                    cur = cur.union(connection[i])
                added = cur.difference(prev)
                prev = cur
            tmp_emails = set()
            for serial in cur:
                tmp_emails = tmp_emails.union(email_book[serial])
            res.extend(sorted(list(tmp_emails)))
            result.append(res)
        return result