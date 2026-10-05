# https://leetcode.com/problems/trapping-rain-water/description/
"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        
        def absolutePositive(x: int):
            if x > 0:
                return x
            return 0
        
        n = len(height)
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        max_l = height[0]
        for i in range(1, n):
            max_left[i] = max_l
            if height[i] > max_l:
                max_l = height[i]
        max_r = height[n-1]
        for j in range(n-2, 0, -1):
            max_right[j] = max_r
            if height[j] > max_r:
                max_r = height[j]
        individual_areas = [absolutePositive(min(max_left[i], max_right[i])-height[i]) for i in range(n)]
        total_area = sum(individual_areas)
        return total_area

def test():
    testcases = [
        {
            "inputs": [[0,1,0,2,1,0,1,3,2,1,2,1]],
            "expected": 6
        },
        {
            "inputs": [[4,2,0,3,2,5]],
            "expected": 9
        }
    ]
    passed, failed = 0, 0
    for testcase in testcases:
        sol = Solution()
        result = sol.trap(*testcase["inputs"])
        if result == testcase["expected"]:
            passed += 1
        else:
            failed += 1
    print("Passed:", passed, "/", len(testcases))
    print("Failed:", failed, "/", len(testcases))
    
test()