class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #implementation 1: kruskal's -> sort all edges, take each in order if they connect nodes
        #s1: define edges and sort them by distance(the cost here)
        edges=[]
        num_nodes=len(points)
        #1000 points/nodes so n-sq is okay
        for i in range(num_nodes):
            for j in range(i+1,num_nodes):
                d=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((d,i,j))
        edges.sort()
        size=[0]*num_nodes
        parent=[i for i in range(num_nodes)]
        # def find(i):
        #     while i!=parent[i]:
        #         parent[i]=parent[parent[i]]#point to grandpa
        #         i=parent[i]#jump two links up-->path halving
        #     return parent[i]
        def find2(i):
            cur=i
            while i!=parent[i]:
                i=parent[i]
            while parent[cur]!=i:
                parent[cur],cur=i,parent[cur]
            return i
        def union(i,j):
            m,n=find2(i),find2(j)
            if m==n:
                return False
            lo,hi=m,n
            if size[m]>size[n]:
                lo,hi=n,m
            parent[lo]=hi
            size[hi]+=size[lo]
            return True
        cnt,total=0,0
        for edge in edges:
            print(edge)
            if union(edge[1],edge[2]):
                print("in for",edge)
                cnt+=1
                total+=edge[0]
                if cnt==num_nodes-1:
                    break
        return total
            