# https://leetcode.com/problems/longest-increasing-subsequence

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x

        return len(tails)

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