class Node:
    def __init__(self):
        self.children=[None]*26
        self.is_end=False

class PrefixTree:

    def __init__(self):
        self.root=Node()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for ch in word:
            i=ord(ch)-ord('a')
            if not cur.children[i]:
                cur.children[i]=Node()
            cur=cur.children[i]
        cur.is_end=True

    def search(self, word: str) -> bool:
        cur=self.root
        for ch in word:
            i=ord(ch)-ord('a')
            if not cur.children[i]:
                return False
            cur=cur.children[i]
        if cur.is_end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for ch in prefix:
            i=ord(ch)-ord('a')
            if not cur.children[i]:
                return False
            cur=cur.children[i]
        return True


        
        