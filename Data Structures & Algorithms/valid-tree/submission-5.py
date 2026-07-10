class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d=defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        visit=set()
        def dfs(node,prev):
            if node in visit: return False
            visit.add(node)
            for nei in d[node]:
                if nei!=prev:
                    if not dfs(nei,node):return False
            return True
        return dfs(0,-1) and len(visit)==n


            

        