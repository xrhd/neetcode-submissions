from collections import defaultdict
import heapq


class Twitter:
    def __init__(self, k=10):
        self.k = k
        self.count = 0
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followeeId in self.follows[userId] | {userId}:
            if self.tweets[followeeId]:
                tweets = self.tweets[followeeId]
                heap += tweets[-self.k :]

        return [tweetId for _, tweetId in heapq.nlargest(self.k, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
