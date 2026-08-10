class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:  
        mp,mp2={},{}
        for pre in prerequisites:
            mp.setdefault(pre[1],[]).append(pre[0])
            mp2[pre[0]]=mp2.get(pre[0],0)+1
        queue=deque()
        for num in range(numCourses):
            if num not in mp2:
                queue.append(num)
        ans=[]
        while queue:
            n=len(queue)
            for _ in range(n):
                el=queue.popleft()
                ans.append(el)
                if el in mp:
                    crs=mp[el]
                    for cr in crs:
                        mp2[cr]-=1
                        if mp2[cr]==0:
                            queue.append(cr)
        if len(ans)==numCourses:
            return ans
        else:
            return []



        