class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(p: str, i: int, j: int) -> bool:
            while i <= j:
                if p[i] != p[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        if not s:
            return True
        if len(s) == 1:
            return True
        n = len(s)
        left, right = 0, n-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
        return True        

def test():
    testcases = [
        {
            "inputs": ["aba"],
            "expected": True
        },
        {
            "inputs": ["abca"],
            "expected": True
        },
        {
            "inputs": ["abc"],
            "expected": False
        }
    ]
    sol = Solution()
    for testcase in testcases:
        result = sol.validPalindrome(*testcase["inputs"])
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