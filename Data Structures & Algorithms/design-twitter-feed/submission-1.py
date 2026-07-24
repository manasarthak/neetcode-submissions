import heapq
class Twitter:

    def __init__(self):
        self.d={}
        self.heap=[]
        self.time=1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.heap,(-self.time,userId,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        temp = list(self.heap)  # Make a copy of the original heap
        heapq.heapify(temp)     # Turn the copy into a valid heap
        while temp and len(res)<10:
            el=heapq.heappop(temp)
            if el[1]==userId: 
                res.append(el[2])
            elif userId in self.d and el[1] in self.d[userId]:
                res.append(el[2])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.d.keys() and followeeId not in self.d[followerId]:
            self.d[followerId].append(followeeId)
        else:
            self.d[followerId]=[followeeId]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.d[followerId]:
            self.d[followerId].remove(followeeId)
