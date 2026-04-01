class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        Dist = []
        for i in range(len(points)):
            dist = 0
            dist = math.sqrt(math.pow(points[i][0], 2) + math.pow(points[i][1], 2))
            Dist.append([(points[i][0], points[i][1]), dist])
        Dist.sort(key=lambda dist: dist[1])
        
        ans = []
        for j in range(k):
            ans.append(Dist[j][0])
        
        return ans
        
