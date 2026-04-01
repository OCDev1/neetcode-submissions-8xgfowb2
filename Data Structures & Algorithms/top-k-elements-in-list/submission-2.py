class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # create a frequency array, bucket q holds nums with frequency q
        freq = [ [] for i in range(len(nums)+1)]

        for n, q in count.items():
            freq[q].append(n) # add n to the list for frequency q
        
        res = []
        for i in range(len(freq)-1, 0, -1):     # go over buckets from high to low
            for n in freq[i]:       # add each value in the bucket to the result
                res.append(n)
                if len(res) >= k:   # if we reached k elements stop and return
                    return res
        