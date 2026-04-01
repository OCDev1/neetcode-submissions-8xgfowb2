class Twitter:

    def __init__(self):
        self.timeStamp = 0
        self.follows = defaultdict(set)  # userId -> set of followeeId
        self.tweets = defaultdict(list)  # userId -> list of [count, tweetIds]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timeStamp, tweetId])
        self.timeStamp -= 1 # we are decrementing so our minheap show most recent at the head

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetch 10 most recent from most to least recent
        # all must be from followed or self
        res = []
        minHeap = []

        self.follows[userId].add(userId)    # user can see his own tweets
        
        for followee in self.follows[userId]:   # iterate over all followees
            if followee in self.tweets:     # if he has any tweets
                i = len(self.tweets[followee]) - 1
                timeStamp, tweetId = self.tweets[followee][i]   # get latest tweet (highest index)
                heapq.heappush(minHeap, [timeStamp, tweetId, followee, i-1])    # [timestamp, tweetId, who posted it, index of next tweet]
        
        while len(res) < 10 and minHeap:
            cur = heapq.heappop(minHeap)
            res.append(cur[1]) # add most recent tweet id to result
            if cur[3] >= 0:
                timeStamp, tweetId = self.tweets[cur[2]][cur[3]]
                heapq.heappush(minHeap, [timeStamp, tweetId, cur[2], cur[3] - 1])  # add this users next recent tweet to heap
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        











