class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # capture the whole integer (e.g. 55)
            ans.append(s[j+1:j+1+length])
            i = j + 1 + length # sets i to next integer
        return ans