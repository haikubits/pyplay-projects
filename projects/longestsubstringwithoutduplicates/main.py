# https://leetcode.com/problems/longest-substring-without-repeating-characters/?difficulty=Medium 19:44

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_length = -float('inf')
        char_map = {}
        left, right = 0, 0
        while right < len(s):
            # check for duplicate
            curr_char = s[right]
            if curr_char not in char_map:
                char_map[curr_char] = right
            else:
                window_length = right - left
                if window_length > max_sub_length:
                    max_sub_length = window_length
                new_left = char_map[curr_char] + 1
                for idx in range(left, new_left):
                    del char_map[s[idx]]
                left = new_left
                char_map[curr_char] = right
            right += 1
        if right-left > max_sub_length:
            max_sub_length = right-left
        return max_sub_length

def test():
    test_cases = [
        {
            "inputs": ["abcabcbb"],
            "expected": 3
        },
        {
            "inputs": ["bbbbb"],
            "expected": 1
        },
        {
            "inputs": ["pwwkew"],
            "expected": 3
        },
        {
            "inputs": ["pwkew"],
            "expected": 4
        },
        {
            "inputs": ["pkew"],
            "expected": 4
        }
    ]
    passed = 0
    failed = 0
    for test_case in test_cases:
        sol = Solution()
        result = sol.lengthOfLongestSubstring(*test_case["inputs"])
        if result == test_case["expected"]:
            passed += 1
        else:
            failed += 1
    print("Passed:", passed, "/", len(test_cases))
    print("Failed:", failed, "/", len(test_cases))

test()