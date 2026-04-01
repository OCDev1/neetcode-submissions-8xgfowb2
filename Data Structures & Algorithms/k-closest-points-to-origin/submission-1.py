import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        Dist = []
        for i in range(len(points)):
            dist = 0
            dist = (math.pow(points[i][0], 2) + math.pow(points[i][1], 2))
            Dist.append([ dist, (points[i][0], points[i][1])])
        heapq.heapify(Dist)
        
        ans = []
        j = 0
        for j in range(k):
            dist, point = heapq.heappop(Dist)
            ans.append(point)
        
        return ans
        
