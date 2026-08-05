class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        lvl = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    lvl.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        depth = -1
        while lvl:
            depth += 1
            ln = len(lvl)
            for _ in range(ln):
                m, n = lvl.popleft()
                for a, b in directions:
                    x, y = m+a, n+b          # was m+b
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        lvl.append((x,y))
                        grid[x][y] = 2
                        fresh -= 1

        if fresh > 0:
            return -1
        return max(depth, 0)