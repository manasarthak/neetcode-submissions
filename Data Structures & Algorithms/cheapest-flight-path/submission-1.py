class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #dfs to keep track of max hops i.e k
        #keep track of on_stack as airporrts we have visited(not a global visited as we can reach the same airport two ways)....
        #create an adjacency list with cost as a (nxt,cost) tuple for O(1) adjacent node traversing
        adj=[[] for _ in range(n)]
        for from_i,to_i,price_i in flights:
            adj[from_i].append((to_i,price_i))
        ans=float('inf')
        def dfs(idx,on_stack,depth,running_cost):#depth is basically len(on_stack) but I keep track for ease
            nonlocal ans
            if depth>k+1 or running_cost>ans:
                return
            if idx in on_stack:#cannot revisiit the same airport twice on same path if we want to minimize total cost and arev free to no lower limit of k
                return
            if idx==dst:
                ans=min(ans,running_cost)
            on_stack.add(idx)
            for nei,cost in adj[idx]:
                dfs(nei,on_stack,depth+1,running_cost+cost)
            on_stack.remove(idx)
            return
        dfs(src,set(),0,0)
        if ans==float('inf'):
            return -1
        else:
            return ans
                
