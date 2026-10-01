from collections import deque
from typing import List

def maximumOfWindow(prices: List[int], k: int):
    if k <= 0:
        return None
    rolling_window = deque(maxlen=k)
    result = []
    for i in range(len(prices)):
        while rolling_window and rolling_window[0] <= i-k:
            rolling_window.popleft()
        
        while rolling_window and prices[rolling_window[-1]] <= prices[i]:
            rolling_window.pop()
        
        rolling_window.append(i)
        
        if i >= k-1:
            result.append(prices[rolling_window[0]])
    return result

def test():
    testcases = [
        {
            "inputs": [[2,3,4,-1,0,4,6,0,10,25,-2], 3],
            "expected": [4, 4, 4, 4, 6, 6, 10, 25, 25]
        },
        {
            "inputs": [[2,3], 3],
            "expected": []
        },
        {
            "inputs": [[], 3],
            "expected": []
        },
        {
            "inputs": [[1, 2, 3, 4], 0],
            "expected": None
        },
        {
            "inputs": [[10, 9, 7, 5, 2, 1, -1], 1],
            "expected": [10, 9, 7, 5, 2, 1, -1]
        },
        {
            "inputs": [[10, 9, 7, 5, 2, 1, -1], 2],
            "expected": [10, 9, 7, 5, 2, 1]
        }
    ]
    passed = 0
    failed = 0
    for testcase in testcases:
        result = maximumOfWindow(*testcase["inputs"])
        if result == testcase["expected"]:
            passed += 1
        else:
            failed += 1
    print("Passed: ", passed, "/", len(testcases))
    print("Failed: ", failed, "/", len(testcases))

test()