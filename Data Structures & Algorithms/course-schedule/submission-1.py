class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        call_stack=[]
        mp={}
        for pre in prerequisites:
             mp.setdefault(pre[0], []).append(pre[1])
        #print(mp)
        def dfs(i):
            if i not in mp.keys():
                return True
            if i in call_stack:
                return False
            call_stack.append(i)
            flag=True
            for j in mp[i]:
                if not dfs(j):
                    return False
            call_stack.pop()
            mp[i]=[]
            return flag
        ans=True
        for num in range(numCourses):
            ans= ans and dfs(num)
        return ans


        