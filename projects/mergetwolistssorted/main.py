# https://leetcode.com/problems/merge-two-sorted-lists/ 3:56

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val})"
    def __eq__(self, other):
        # If the other object is not a ListNode, they are not equal
        if not isinstance(other, ListNode):
            return False
            
        current_self = self
        current_other = other
        
        # Traverse both linked lists simultaneously
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
            
        # Both must reach the end (None) at the same time to be equal
        return current_self is None and current_other is None

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        return head.next

def list_to_linkedList(inputList = []):
    if not inputList:
        return None
    else:
        head = ListNode(inputList[0])
        curr = head
        for item in inputList[1:]:
            curr.next = ListNode(item)
            curr = curr.next
        return head

def printList(head: ListNode):
    result = f"Node({head.val})"
    curr = head.next
    while curr:
        result += "->" + f"Node({curr.val})"
        curr = curr.next
        return result
    
def test():
    test_cases = [
        {
            "inputs": [[1,2,4],[1,3,4]],
            "expected": [1,1,2,3,4,4]
        },
        {
            "inputs": [[], []],
            "expected": []
        },
        {
            "inputs": [[], [0]],
            "expected": [0]
        }
    ]
    passed = 0
    failed = 0
    for test_case in test_cases:
        sol = Solution()
        inputs = [list_to_linkedList(item) for item in test_case["inputs"]]
        expected = list_to_linkedList(test_case["expected"])
        #print("TestCase:", [printList(inputItem) if inputItem else "None" for inputItem in inputs], printList(expected) if expected else "None")
        result = sol.mergeTwoLists(*inputs)
        #print("Actual Result:", printList(result) if result else "None")
        if result == expected:
            passed += 1
        else:
            failed += 1
    print("Passed:", passed, "/", len(test_cases))
    print("Failed:", failed, "/", len(test_cases))

test()