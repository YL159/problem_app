'''
Leetcode 1024. Video Stitching
Given the (start, end) series of clips, find the min # of clips that can cover [0, time] interval

Here provides a state machine greedy solution.
Decides a current holding end time, check how far away other clips can make while 'hooking' up with current clip
Implicitly select the hooked clip that provides the farthest end.
And set this end as new holding position, to reduce total # of clips to be selected.
'''
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        res = 1
        # cur is the current holding end time
        # nex is the largest end time if a clip starts <= cur
        cur, nex = 0, 0
        for start, end in clips:
            # if a start is greater than farthest reachable, there must be a gap
            if start > nex:
                return -1
            # a clip 'hooks' with current end time, update farthest end time
            if start <= cur:
                if end > nex:
                    nex = end
            # a clip off the hook and provides greater end, include 'it' or 1 of its 'series'
            elif end > nex:
                # greedy choice, actually select the interval provides the farthest reachable end
                # and make the holding end same as this farthest end, to reduce clip total #
                cur = nex
                nex = end
                res += 1
            # check if farthest reachable covers target time
            if nex >= time:
                return res
        return res if nex >= time else -1
            