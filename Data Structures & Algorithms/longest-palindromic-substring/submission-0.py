class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        n=len(s)
        n1=0
        for i in range(n):
            #check odd length/centered palindrome max length with this character as center
            temp=1
            j=1
            while i-j>=0 and i+j<n:
                if s[i-j]==s[i+j]:
                    temp+=2
                    j+=1
                else:
                    break
            if temp>n1:
                ans=s[i-j+1:i+j]
                n1=temp
            #for even length palindrome; assume idx,idx+1 to be center candidates
            if i<n-1 and s[i]==s[i+1]:
                temp=2
                j=1
                while i-j>=0 and i+j+1<n:
                    if s[i-j]==s[i+j+1]:
                        temp+=2
                        j+=1
                    else:
                        break
                if temp>n1:
                    ans=s[i-j+1:i+j+1]
                    n1=temp
        return ans
