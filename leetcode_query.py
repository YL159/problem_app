import urllib3 as ul
import re
from typing import List


# wrapper class for question meta info, implement attr get interface
class Question:
    def __init__(self, data: dict):
        self._data = data

    @property
    def id(self) -> int:
        return int(self._data["id"])

    @property
    def title(self) -> str:
        return self._data["title"]
    
    @property
    def url(self) -> str:
        return f"https://leetcode.com/problems/{self._data["titleSlug"]}"

    @property
    def difficulty(self) -> str:
        return self._data["difficulty"]
    
    @property
    def tags(self) -> list:
        return [tag["name"] for tag in self._data["topicTags"] if tag["name"] in all_tags]


# make graphql query of leetcode question title slug
# q number not searchable if not logged in
# return basic info of the question
def query_leet(title_slug: str) -> Question | None:
    leetcode = "https://leetcode.com/graphql"

    # header as browser request
    headers = {
    "Content-Type": "application/json",
    "User-Agent": "Chrome/120.0.0.0",
    "Referer": "https://leetcode.com"
    }

    query = {
        "query": """
            query questionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    title
                    titleSlug
                    questionId
                    difficulty
                    topicTags {
                    name
                    }
                }
            }
        """,
        "variables": {
            "titleSlug": f"{title_slug}"
        }
    }
    # print(title_slug)
    # make POST request
    try:
        response = ul.request("POST", leetcode, json=query, headers=headers)

        if response.status == 200:
            data = response.json()
            detail = data["data"]["question"]
            # print(detail)
            return Question(detail)
        else:
            print(f"Failed to fetch question {title_slug}, status {response.status}")
            print(response.data)
    except Exception as e:
        print(f"Error: {e}")


# tags ordered by problem count (popularity), keep this order
all_tags = ['Array', 'String', 'Hash Table', 'Math', 'Dynamic Programming', \
            'Sorting', 'Greedy', 'Depth-First Search', 'Binary Search', 'Database', \
            'Bit Manipulation', 'Matrix', 'Tree', 'Breadth-First Search', 'Prefix Sum', \
            'Two Pointers', 'Heap (Priority Queue)', 'Simulation', 'Counting', \
            'Graph Theory', 'Binary Tree', 'Stack', 'Sliding Window', 'Enumeration', \
            'Design', 'Backtracking', 'Number Theory', 'Union-Find', 'Linked List', \
            'Segment Tree', 'Ordered Set', 'Monotonic Stack', 'Divide and Conquer', \
            'Combinatorics', 'Trie', 'Queue', 'Bitmask', 'Recursion', 'Geometry', \
            'Binary Indexed Tree', 'Hash Function', 'Memoization', 'Binary Search Tree', \
            'Topological Sort', 'Shortest Path', 'String Matching', 'Rolling Hash', \
            'Game Theory', 'Monotonic Queue', 'Interactive', 'Data Stream', 'Brainteaser', \
            'Doubly-Linked List', 'Merge Sort', 'Randomized', 'Counting Sort', 'Iterator', \
            'Concurrency', 'Quickselect', 'Suffix Array', 'Sweep Line', \
            'Probability and Statistics', 'Minimum Spanning Tree', 'Bucket Sort']


if __name__ == "__main__":

    title = "longest-substring-without-repeating-characters"

    question = query_leet(title)
    print(question.tags)