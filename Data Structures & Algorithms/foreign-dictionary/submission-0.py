class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}  # for each letter we create a set

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""   # invalid sorting
            
            # populating dictionary
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}    # keep track of visited
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True    # mark as visited for cycle detection

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):   # if dfs returns true there is a cycle
                return ""

        res.reverse()   # because dfs returns the reverse order
        return "".join(res)