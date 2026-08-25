class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #implementation 2: bellman ford...which is after k runs every node that is at least k distance from starting node 
        min_cost=[float('inf') for _ in range(n)]
        min_cost[src]=0
        for _ in range(k+1):
            temp=min_cost[:]
            for from_i,to_i,price_i in flights:
                temp[to_i]=min(min_cost[from_i]+price_i,temp[to_i])
            min_cost=temp
        if min_cost[dst]==float('inf'):
            return -1
        else:
            return min_cost[dst]
