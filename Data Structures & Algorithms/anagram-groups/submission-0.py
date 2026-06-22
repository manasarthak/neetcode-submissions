class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       res=[]
       hsh={}
       freq=[0]*26
       j=0
       for st in strs:
        for ch in st:
            freq[ord(ch)-ord('a')]+=1
        key=""
        for i in range(len(freq)):
            if freq[i]>0:
                key+=chr(i+65)+str(freq[i])
        #print(key)
        if key in hsh.keys():
            res[hsh[key]].append(st)
        else:
            hsh[key]=j
            res.append([st])
            j+=1
        freq=[0]*26
       return res
       
    
        

                


        