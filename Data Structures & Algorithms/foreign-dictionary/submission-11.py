class Solution:
    def foreignDictionary(self, w: List[str]) -> str:
        c={x:set() for _ in w for x in _}
        for i in range(len(w)-1):
            w1,w2=w[i],w[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    c[w1[j]].add(w2[j])
                    break  
        visited={}
        res=[]
        def dfs(v):
            if v in visited:
                return visited[v]
            visited[v]=True
            for nei in c[v]:
                if dfs(nei): return True
            res.append(v)
            visited[v]=False
            return False
        for i in c:
            if dfs(i):return ''
        res.reverse()
        return ''.join(res)

            
        