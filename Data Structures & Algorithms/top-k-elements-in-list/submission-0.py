class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        val=[[] for i in range(len(nums)+1)]
        for i in nums:
            d[i]=1+d.get(i,0)
        for n,c in d.items():
            val[c].append(n)
        res=[]
        for i in range(len(val)-1,0,-1):
            for j in val[i]:
                res.append(j)
                if len(res)==k:
                    return res