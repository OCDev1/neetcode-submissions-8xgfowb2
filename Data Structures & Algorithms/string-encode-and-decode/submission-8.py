class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            length = str(len(word))
            encoded_string = encoded_string + length + "#" + word
        encoded_string = encoded_string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        list = []
        word = ""
        pointer = 0
        while pointer < len(s):
            n = ""
            while s[pointer] != "#":
                n = n + s[pointer]
                pointer = pointer+1
            word_len = int(n)
            start = pointer+1
            end = pointer+word_len+1
            for i in range(start, end):
                word = word + s[i]
            list.append(word)
            word = ""
            pointer = end
        return list