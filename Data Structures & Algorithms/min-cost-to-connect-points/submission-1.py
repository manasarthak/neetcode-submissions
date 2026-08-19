class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        in_tree = [False] * n
        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for v in range(n):                       # O(n) scan instead of heap pop
                if not in_tree[v] and (u == -1 or min_dist[v] < min_dist[u]):
                    u = v
            in_tree[u] = True
            total += min_dist[u]
            xu, yu = points[u]
            for v in range(n):                       # relax, computing distance on the fly
                if not in_tree[v]:
                    d = abs(xu - points[v][0]) + abs(yu - points[v][1])
                    if d < min_dist[v]:
                        min_dist[v] = d
        return total