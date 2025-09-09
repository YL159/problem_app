'''
Leetcode 2327. Number of People Aware of a Secret
On day 1, 1 person knows a secret.
After "delay" days once they knows the secret, they can tell a new person the secret each day.
After "forget" days once they know the secret, they forget the secret.
Find how many people know the secret on nth day

Secret's propagation window for each person is during [know+delay, know+forget]
And each person's knowing window is [know, know+forget]
Thus we can keep track of each batch of new people knowing secrets
and use line sweep to track knowing and propagating increment/decrement

Time O(n), Space O(n)
'''
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        # line sweep on day x's
        # increment/decrement of people know
        know = [0] * (n+forget+1)
        know[1], know[1 + forget] = 1, -1
        # increment/decrement of people can tell secrets
        tell = [0] * (n+forget+1)
        tell[1 + delay], tell[1 + forget] = 1, -1
        # on day x, k people know, and t people can tell, k >= t
        k, t = 0, 0
        for day in range(1, n+1):
            # line sweep today's can-tell count
            t += tell[day]
            # thus today t new people will know secret, and they forget at today+forget
            know[day] += t
            know[day + forget] -= t
            # same for these t people's can-tell window
            tell[day + delay] += t
            tell[day + forget] -= t
            # today's knowing count line sweep
            k += know[day]
            k %= mod
        return k
