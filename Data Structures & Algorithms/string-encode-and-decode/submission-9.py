class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        j = 0
        
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j
            j = i
            
        return res