import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.h = nums
        self.k=k
        while len(self.h) > k:
            heapq.heappop(self.h)
        

    def add(self, val: int) -> int:
        if len(self.h)<self.k:
            heapq.heappush(self.h,val)
        elif val>self.h[0]:
            heapq.heapreplace(self.h,val)
        return self.h[0]
        
