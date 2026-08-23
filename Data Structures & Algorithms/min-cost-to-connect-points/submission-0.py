import heapq


class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


def kruskalsMST(edges, n):
    minHeap = []
    for n1, n2, weight in edges:
        heapq.heappush(minHeap, [weight, n1, n2])

    unionFind = UnionFind(n)
    mst = []
    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)
        if not unionFind.union(n1, n2):
            continue
        mst.append([n1, n2, weight])
    return mst


def manhattan_distance(p1, p2):
    dim = len(p1)
    dis = 0
    for i in range(dim):
        dis += abs(p1[i] - p2[i])

    return dis


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Kruskal's solution"""
        n = len(points)
        edges = [
            (i + 1, j + 1, manhattan_distance(points[i], points[j]))
            for i in range(n - 1)
            for j in range(1, n)
        ]

        mst = kruskalsMST(edges, n)
        return sum((edge[-1] for edge in mst))
