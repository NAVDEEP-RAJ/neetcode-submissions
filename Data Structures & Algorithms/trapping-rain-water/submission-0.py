class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft=maxright=0
        l=[0]*n
        r=[0]*n
        for i in range(len(height)):
            j=-i-1
            l[i]=maxleft
            r[j]=maxright
            maxleft=max(maxleft,height[i])
            maxright=max(maxright,height[j])
        summ=0
        for i in range(n):
            wat=min(l[i],r[i])-height[i]
            summ+=max(0,wat)
        return summ

        