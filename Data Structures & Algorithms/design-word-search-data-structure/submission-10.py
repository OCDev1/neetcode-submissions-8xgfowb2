class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode() # add letter to path
            cur = cur.children[char]
        cur.isWord = True
                
    def search(self, word: str) -> bool:
        cur = self.root
        
        for i in range(len(word)):
            if word[i] in cur.children:
                cur = cur.children[word[i]]    # continue searching
            elif word[i] == ".":
                # search all kids
                for child in cur.children.values():     # at most 26 so O(1)
                    if self.dot_search(child, word[i+1:]):
                        return True
                return False
            else:
                return False    # cannot progress, the word doesnt exist in the trie.
        return cur.isWord

    def dot_search(self, root, word):
        cur = root
        print(cur)
        for j in range(len(word)):
            if word[j] in cur.children:
                cur = cur.children[word[j]]    # continue searching
            elif word[j] == ".":
                # search all kids
                for child in cur.children.values():     # at most 26 so O(1)
                    if self.dot_search(child, word[j+1:]):
                        return True
                return False
            else:
                return False    # cannot progress, the word doesnt exist in the trie.
        return cur.isWord




