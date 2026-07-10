class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        visit=set()
        def dfs(i,prev):
            if i in visit:return
            visit.add(i)
            for nei in d[i]:
                if nei!=prev:
                    dfs(nei,i)
        count=0
        for j in range(n):
            if j not in visit:
                dfs(j,-1)
                count+=1
        return count
        