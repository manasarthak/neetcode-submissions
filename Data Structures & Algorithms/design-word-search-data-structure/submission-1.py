from collections import deque


class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False



class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for ch in word:
            i=ord(ch)-ord('a')
            if not cur.children[i]:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        cur.isEnd=True
            
        

    def search(self, word: str) -> bool:
        queue=deque([self.root])
        for i in range(len(word)):
            ch=word[i]
            n=len(queue)
            print(n,ch)
            if ch=='.':
                for j in range(n):
                    el=queue.popleft()
                    for k in range(26):
                        if el.children[k]:
                            if i == len(word) - 1 and el.children[k].isEnd:
                                return True
                            queue.append(el.children[k])
            else:
                idx=ord(ch)-ord('a')
                for j in range(n):
                    el=queue.popleft()
                    if el.children[idx]:
                        if i ==len(word)-1 and el.children[idx].isEnd:
                            return True
                        queue.append(el.children[idx])
            if not queue:
                return False
        return False

                    


        
