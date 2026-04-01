class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        edge_map = collections.defaultdict(list)
        
        visited = set(beginWord)
      
        for word in wordList:
            # for each pattern we append the list of words that match it, e.g. for dog -> create lists *og, d*g, do*
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                edge_map[pattern].append(word)
        
        q = deque([beginWord])  # start with the beginWord.
        
        res = 1
        
        # run the BFS
        while q:
            for i in range(len(q)): # run current layer of BFS
                word = q.popleft()
                if word == endWord:     # if we reached goal word we are done.
                    return res

                for j in range(len(word)):  # loop to check for children of current word
                    pattern = word[:j] + "*" + word[j+1:]

                    for child in edge_map[pattern]: # for all children nodes of current word
                        if child not in visited:    # if we weren't already there - add to queue.
                            visited.add(child)
                            q.append(child)

            res += 1    # next layer of BFS
        return 0    # could not reach endWord





