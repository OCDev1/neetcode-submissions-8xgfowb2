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
        # count chars in first window
        win_count = Counter(s2[start:end])
        # slide the window
        while end < len(s2):
            if win_count == count:
                return True
            else:       # move the window by 1, and update the hash maps
                win_count[s2[start]] -=1
                win_count[s2[end]] +=1
                start+=1
                end+=1
        # check for final window position
        if win_count == count:
            return True
        return False