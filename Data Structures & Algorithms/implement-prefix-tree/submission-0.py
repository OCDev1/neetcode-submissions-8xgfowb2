class TrieNode:
    def __init__(self):
        self.children = {}  # child nodes
        self.endOfWord = False  # is this the final letter in a word?

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return cur.endOfWord    # is the place we just stopped at an end of word? if yes then this word is in our trie

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return True
        