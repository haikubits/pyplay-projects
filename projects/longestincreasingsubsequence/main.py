# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

def test():
    testcases = [
        {
            "inputs": [[10,9,2,5,3,7,101,18]],
            "expected": 4
        },
        {
            "inputs": [[0,1,0,3,2,3]],
            "expected": 4
        },
        {
            "inputs": [[7,7,7,7,7,7,7]],
            "expected": 1
        }
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.lengthOfLIS(*testcase["inputs"])
        if result == testcase["expected"]:
            testcase["status"] = "passed"
        else:
            testcase["status"] = "failed"
            testcase["output"] = result
    print("Passed: ", len([x for x in testcases if x["status"]=="passed"]), "/", len(testcases))
    print("Failed: ", len([x for x in testcases if x["status"]=="failed"]), "/", len(testcases))
    for testcase in [x for x in testcases if x["status"]=="failed"]:
        print("Input:", testcase["inputs"])
        print("Expected:", testcase["expected"])
        print("Output:", testcase["output"])
        
test()