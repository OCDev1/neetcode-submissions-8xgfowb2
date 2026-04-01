class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        short_str = s1
        long_str = s2

        # count chars in short string
        count = Counter(s1)
        # get size of sliding window
        win_size = len(s1)
        # start and end indices of sliding window
        start = 0
        end = len(s1)
        matches = 0
        # count chars in first window
        win_count = Counter(s2[0:len(s1)])
        for char in count:
            if win_count[char] == count[char]:
                matches+=1

        # slide the window
        for end in range(len(s1),len(s2)):
            if matches == len(count):
                return True

            # handle incoming char
            char_in = s2[end]
            if char_in in count:
                win_count[char_in]+=1
                if win_count[char_in] == count[char_in]:
                    matches+=1
                elif win_count[char_in] - 1 == count[char_in]:
                    matches -= 1

            # handle outgoing char
            char_out = s2[start]
            if char_out in count:
                if win_count[char_out] == count[char_out]:
                    matches -= 1
                win_count[char_out] -= 1
                if win_count[char_out] == count[char_out]:
                    matches += 1

            start+=1
        return matches == len(count)