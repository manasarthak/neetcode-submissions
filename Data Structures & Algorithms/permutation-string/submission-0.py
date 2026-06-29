class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n2<n1:
            return False
        mp={}
        temp={}
        for i in range(n1):
            mp[s1[i]]=1+mp.get(s1[i],0)
            temp[s2[i]]=1+temp.get(s2[i],0)
        if mp==temp:
            return True
        lo=1
        while lo<=n2-n1:
            temp[s2[lo-1]]-=1
            if temp[s2[lo-1]]==0:
                del temp[s2[lo-1]]
            temp[s2[lo+n1-1]]=temp.get(s2[lo+n1-1],0)+1
            if temp==mp:
                return True
            lo+=1    
        return False
            


        
        