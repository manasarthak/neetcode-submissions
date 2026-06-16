class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=dict()
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for ch in t:
            if ch not in d.keys():
                return False
            else:
                d[ch]-=1
                if d[ch]<0:
                    return False
        for key in d.keys():
            if d[key]>0:
                return False
        return True
        