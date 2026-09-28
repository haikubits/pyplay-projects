# https://leetcode.com/problems/invert-binary-tree/ 1:35

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def build_level_order(arr, i, n) -> TreeNode:
    root = None
    # Base case for recursion
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        # Insert left child
        root.left = build_level_order(arr, 2 * i + 1, n)
        # Insert right child
        root.right = build_level_order(arr, 2 * i + 2, n)
    return root

from collections import deque

def tree_to_array(root: TreeNode):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
            
    # Clean up trailing 'None' values representing empty leaves at the bottom
    while result and result[-1] is None:
        result.pop()
        
    return result


def test():
    testCases = [
        {
            "input": [4,2,7,1,3,6,9],
            "expected": [4,7,2,9,6,3,1]
        },
        {
            "input": [2, 1, 3],
            "expected": [2, 3, 1]
        },
        {
            "input": [],
            "expected": []
        }
    ]
    passed = 0
    failed = 0
    for testCase in testCases:
        inputNode = build_level_order(testCase["input"], 0, len(testCase["input"]))
        sol = Solution()
        result = sol.invertTree(inputNode)
        result_array = tree_to_array(result)
        if result_array == testCase["expected"]:
            passed += 1
        else:
            failed += 1
    print("Passed:", passed, "/", len(testCases))
    print("Failed:", failed, "/", len(testCases))

test()