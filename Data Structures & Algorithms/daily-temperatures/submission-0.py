class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        cand=[[temperatures[-1],len(temperatures)-1]]
        for i in range(len(temperatures)-2,-1,-1):
            while cand:
                if cand[-1][0]>temperatures[i]:
                    res[i]=cand[-1][1]-i
                    break
                else:
                    cand.pop()
            cand.append([temperatures[i],i])
            print(cand)
        return res

        