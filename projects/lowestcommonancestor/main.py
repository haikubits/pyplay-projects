# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ 7:15

# Remember that for the opposite sides of root, p & q both could be on either side p < root < q or p > root > q

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # start with root if p and q are on same side of root, then go one level down on that side, if p and q are on different sides of root, then root is the LCA. If either p or q is root, then root is the LCA.
        if p.val == root.val or q.val == root.val:
            return root
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

def test():
    testCases = [
        {
            "inputs": [TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(3), TreeNode(1)],
            "expected": TreeNode(2)
        },
        {
            "inputs": [TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(8)],
            "expected": TreeNode(6)
        },
        {
            "inputs": [TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(4)],
            "expected": TreeNode(2)
        },
        {
            "inputs": [TreeNode(2, TreeNode(1)), TreeNode(2), TreeNode(1)],
            "expected": TreeNode(2)
        }
    ]
    passed = 0
    failed = 0
    for testcase in testCases:
        sol = Solution()
        result = sol.lowestCommonAncestor(*testcase["inputs"])
        if result.val == testcase["expected"].val:
            passed += 1
        else:
            failed += 1
    print("Passed:", passed, "/", len(testCases))
    print("Failed:", failed, "/", len(testCases))

test()