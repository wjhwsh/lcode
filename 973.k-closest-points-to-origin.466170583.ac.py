class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        
        def distance(point):
            return point[0] * point[0] + point[1] * point[1]
        
        def partition(left, right, pivot):
            points[pivot], points[right] = points[right], points[pivot]
            storedIndex = left
            i = left
            while i < right:
                if distance(points[i]) < distance(points[right]):
                    points[storedIndex], points[i] = points[i], points[storedIndex]
                    storedIndex += 1
                i += 1
            points[storedIndex], points[right] = points[right], points[storedIndex]
            return storedIndex
        
        def sort(left, right, k):
            if left >= right:
                return
            mid = random.randint(left, right)
            mid = partition(left, right, mid)
            if k > mid - left + 1:
                sort(mid+1, right, k - (mid - left +1))
            elif k < mid - left + 1:
                sort(left, mid - 1, k)  
        
        sort(0, len(points) - 1, k)
        return points[:k]
