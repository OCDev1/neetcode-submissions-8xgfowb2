class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i]:
                cur = cur.children[i]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i]:
                cur = cur.children[i]
            else:
                return False
        return True
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False