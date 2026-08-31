class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        n1=0
        for i in range(n):
            #check odd length/centered palindrome max length with this character as center
            temp=1
            j=1
            n1+=1
            while i-j>=0 and i+j<n:
                if s[i-j]==s[i+j]:
                    temp+=2
                    j+=1
                    n1+=1
                else:
                    break
            #for even length palindrome; assume idx,idx+1 to be center candidates
            if i<n-1 and s[i]==s[i+1]:
                temp=2
                j=1
                n1+=1
                while i-j>=0 and i+j+1<n:
                    if s[i-j]==s[i+j+1]:
                        temp+=2
                        j+=1
                        n1+=1
                    else:
                        break
        return n1
