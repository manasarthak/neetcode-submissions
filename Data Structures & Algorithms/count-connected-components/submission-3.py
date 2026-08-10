class DUS:
    def __init__(self,n):
        self.components=n
        self.parent=[i for i in range(n)]
        self.size=[1]*n
    def find(self, node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self, n1,n2):
        u,v=self.find(n1),self.find(n2)
        if u==v:
            return
        #print("enter")
        m,n=self.size[n1],self.size[n2]
        if m<=n:
            u,v=v,u
        self.size[u]+=self.size[v]
        self.parent[v]=self.parent[u]
        self.components-=1
        return

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf_obj=DUS(n)
        for edg in edges:
            uf_obj.union(edg[0],edg[1])
            #print(uf_obj.parent)
        return uf_obj.components
            
        