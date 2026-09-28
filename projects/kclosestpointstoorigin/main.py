#https://leetcode.com/problems/k-closest-points-to-origin

import random

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist_sq(point: list[int]) -> int:
            return point[0]*point[0] + point[1]*point[1]
        
        def quickselect(left, right):
            if left >= right:
                return
            
            pivot_idx = random.randint(left, right)
            pivot_dist = dist_sq(points[pivot_idx])

            points[pivot_idx], points[right] = points[right], points[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if dist_sq(points[i]) < pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
            
            points[store_idx], points[right] = points[right], points[store_idx]

            if store_idx == k:
                return
            elif store_idx < k:
                quickselect(store_idx + 1, right)
            else:
                quickselect(left, store_idx-1)
        quickselect(0, len(points)-1)
        return points[:k]