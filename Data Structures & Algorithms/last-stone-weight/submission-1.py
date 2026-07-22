import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones1=[-x for x in stones]
        heapq.heapify(stones1)
        while len(stones1)>1:
            el1=-heapq.heappop(stones1)
            el2=-heapq.heappop(stones1)
            if el1==el2:
                continue
            elif el1>el2:
                heapq.heappush(stones1,el2-el1)
            else:
                heapq.heappush(stones1,el1-el2)
        if not stones1:
            return 0
        return -stones1[0]
        