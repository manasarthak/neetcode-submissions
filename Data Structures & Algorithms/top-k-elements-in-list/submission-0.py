class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}

        for n in nums:
            if n in d.keys():
                d[n]+=1
            else:
                d[n]=1
        freq=list(d.values())
        freq.sort()
        s=set(freq[-k:])
        res=[]
        for key in d.keys():
            if d[key] in s:
                res.append(key)
        return res

        