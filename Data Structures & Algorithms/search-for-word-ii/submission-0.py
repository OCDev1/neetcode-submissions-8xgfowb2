class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)
        
        R = len(board)
        C = len(board[0])
        
        res, visit = set(), set()

        def helper(row, col, node, word):
            if (row >= R or col >= C or row < 0 or col < 0 # out of bounds
                or (row,col) in visit    # already been here in current word
                or board[row][col] not in node.children
            ):
                return  # isn't part of a word in the trie

            visit.add((row,col))    # mark as visited
            node = node.children[board[row][col]]   # update node
            word = word + board[row][col]   # update word
            
            if node.endOfWord:  # if the word is in the tree, add it
                res.add(word)

            # recursive calls:
            helper(row + 1, col , node , word)
            helper(row - 1, col , node , word)
            helper(row , col+ 1 , node , word)
            helper(row , col-1 , node , word)

            # after we finished calls for cell
            visit.remove((row,col))

        for r in range(R):
            for c in range(C):
                helper(r, c, root, "")

        return list(res)

