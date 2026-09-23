class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #at each start we can reduce by one of the acndidate words and try to make up the next sequence of words
        #each step we get to can lead to n=len(dict) choices 200 length and lead to 100^200 choices at each step worset case scenario
        #caveat is they only contain english letters so at each step worst case in reality is only 26 choices and we realistically go down only 1 in case opf single letters 
        #if two ways get to the same point we can reduce redundant computization using memoization but thisis a boolean question as soon as we get to idx=len(s) we say true and break the whole thing; use a global lock to further calls 
        n=len(s)
        #flag only helps after success if for a particular idx we have explored all the possibilieties befiore and arriving at a fauiling branch we explore again
        memo={}
        def dfs(idx):
            if idx==n:
                return True
            if idx in memo:
                return memo[idx]
            for word in wordDict:
                l=len(word)
                if s[idx:idx+l]==word and dfs(idx+l):
                    memo[idx]=True
                    return True
            memo[idx]=False
            return False
        return dfs(0)
            
        