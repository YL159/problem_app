'''
Leetcode 2116. Check if a Parentheses String Can Be Valid
Given a string of ( and ), and a string of 01 of same length. Match them head to toe.
At 1, the parenthesis is locked. At 0 you can change it to any (/)
Check if this str can be a valid paren str.

Since we don't know if 0 can greedily pair with prev 0 or 1-(, or remain ( to pair with future 1-)
We can greedily pair with prev 0 or 1-(
	AND record this pair, in order to open it and make 2x ( to pair with future 0-) or 1-)
Thus we pair along the way as many as possible, while keeping remaining ( as few as possible.

Check the code comments for state machine operation details.
'''
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        # remaining left (. pairs of () eliminated, the ) is 0-unlocked
        left, pairs = 0, 0
        for i in range(len(s)):
            if locked[i] == '1':
                # locked (, directly add to ( reserve
                if s[i] == '(':
                    left += 1
                # locked ), must pair with reserved (
                elif left:
                    left -= 1
                # locked ) but no reserved (, transform prev 1 pair into ((
                elif pairs:
                    pairs -= 1
                    left += 1
                # no pairs and no reserved (, False!
                else:
                    return False
            # unlocked pos, translate as ) if any reserved (, add to pairs
            elif left:
                pairs += 1
                left -= 1
            # unlocked pos but no reserved (, translate as (
            else:
                left += 1
        # valid if no reserved ( left. Cus all ( are supposed to be greedily paired
        return left == 0

