class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for i in range (len(s)):
            if s[i].isalnum():
                temp.append(s[i].lower())
        lo,hi=0,len(temp)-1
        print(temp)
        while lo<hi:
            if temp[lo]!=temp[hi]:
                return False
            hi-=1
            lo+=1
        return True
            
        