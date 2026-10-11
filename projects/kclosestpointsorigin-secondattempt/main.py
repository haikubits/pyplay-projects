print("Hello World")



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