import heapq
class MedianFinder:

    def __init__(self):
        self.heap=[]
        self.size=0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap,num)
        self.size+=1
        

    def findMedian(self) -> float:
        temp=list(self.heap)
        heapq.heapify(temp)
        print(temp)
        for i in range((self.size//2)-1):
            print('in')
            heapq.heappop(temp)
        print(temp)
        if self.size%2==0:   
            el1=heapq.heappop(temp)
            el2=heapq.heappop(temp)
            return (el1+el2)/2.0
        else:
            if self.size>1:
                heapq.heappop(temp)
            return float(heapq.heappop(temp))



        
        