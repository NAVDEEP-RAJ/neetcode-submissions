"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        s,e,res,c=0,0,0,0
        while s<len(st):
            if st[s]<end[e]:
                s+=1
                c+=1
            else:
                e+=1
                c-=1
            res=max(res,c)
        return res