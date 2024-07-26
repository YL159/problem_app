'''
Leetcode 1823. Find the Winner of the Circular Game
N people form a circle, every kth clockwise person get out of the circle till 1 person left.
Find the winner's initial label. 1 indexed.

Here is an O(n) time and O(1) space solution.
If every time some1 out of the circle, previous k-1 people move to the end of the people list
Then the new n-1 person game winner's POSITION(index) is the same as n-1 people game's winner ID

Consider 3 ppl [1,2,3] game, k=2:
index: 0,1,2 -> 0,2 -> k-1_move_to_end -> 2,0 -> 2.
for 3 ppl winner is index 2

For 4 ppl k=2:
index: 0,1,2,3 -> 0,2,3 -> k-1_move -> 2,3,0
Now it's again 3 ppl game. From previous result, [2,3,0] got winner POSITION at 2, i.e. ID 0
But here ID 0 was initially at POSITION 0, thus construct POSITION->ID relation, reverse the k-1(also k) move

Final result +1 to make it 1 indexed.
'''

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner_index = 0
        for i in range(2, n+1):
            # this game's winner ID is based on previous n-1 person winner POSITION
            winner_index = (winner_index + k) % i
        return winner_index + 1