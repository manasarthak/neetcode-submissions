class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #will bfs work here; the compute is revolvinga round whether str1 and str2 have only one diferent character? what could be the most efficient way to do that? i will start with direct comparison
        queue=deque([beginWord])
        visited=set([beginWord])
        ans=1
        def count_diff(str1,str2):
            n=len(str1)
            mis_match=0
            for i in range(n):
                if str1[i]!=str2[i]:
                    mis_match+=1
                    if mis_match>1:
                        return False
            return mis_match==1

        while queue:
            ans+=1
            n=len(queue)
            for _ in range(n):
                word=queue.popleft()
                for j in range(len(wordList)):
                    n_word=wordList[j]
                    if n_word not in visited and count_diff(word,n_word):
                        visited.add(n_word)
                        if n_word==endWord:
                            return ans
                        queue.append(n_word)
        return 0



        