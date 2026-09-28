# https://leetcode.com/problems/minimum-window-substring/description/?difficulty=Medium 26:55

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        min_window, min_left, min_right = float('inf'), 0, 0
        need = len(t_dict)
        have = 0
        s_counter = {}
        left, right = 0, 0
        
        while right < len(s):
            char_r = s[right]
            s_counter[char_r] = s_counter.get(char_r, 0) + 1
            if char_r in t_dict and s_counter[char_r] == t_dict[char_r]:
                have += 1
            
            # check if window matches
            if have == need:
                # shrink the window from left (minimum window)
                while left < right:
                    char_l = s[left]

                    if char_l in t_dict and s_counter[char_l] == t_dict[char_l]:
                            break
                    else:
                        s_counter[char_l] -= 1
                    left += 1
                window_size = right-left+1
                if window_size < min_window:
                    min_window, min_left, min_right = window_size, left, right
            
            right += 1

        if min_window != float('inf'):
            return s[min_left:min_right+1]
        return ""

def test():
    test_cases = [
        {
            "inputs" : ["ADOBECODEBANC", "ABC"],
            "expected": "BANC"
        },
        {
            "inputs" : ["a", "a"],
            "expected": "a"
        },
        {
            "inputs" : ["a", "aa"],
            "expected": ""
        }
	]
    passed = 0
    failed = 0
    for test_case in test_cases:
        sol = Solution()
        result = sol.minWindow(*test_case["inputs"])
        if result == test_case["expected"]:
            passed += 1
        else:
            failed += 1
    print("Passed:", passed,"/", len(test_cases))
    print("Failed:", failed,"/", len(test_cases))

test()