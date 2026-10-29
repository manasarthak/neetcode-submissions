class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans,l=s[0],1
        for idx in range(n):
            #case 1: consider idx as the middle index of the palindrome
            l1,shift=1,1
            while idx-shift>-1 and idx+shift<n and s[idx-shift]==s[idx+shift]:
                l1+=2
                shift+=1
            #case 2 : consider idx and idx+1 as the joint middle of an even length palindrome
            # thats only possible if s[idx] and s[idx+1] are the same character
            l2,shift2=1,1
            if idx+1<n and s[idx]==s[idx+1]:
                l2+=1
                while idx-shift2>-1 and idx+shift2+1<n and s[idx-shift2]==s[idx+shift2+1]:
                    l2+=2
                    shift2+=1
            if l1>l:
                ans=s[idx-shift+1:idx+shift]
                l=l1
            if l2>l:
                ans=s[idx-shift2+1:idx+shift2+1]
                l=l2
        return ans



        