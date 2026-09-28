# https://leetcode.com/problems/merge-k-sorted-lists/description/?difficulty=Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        n = len(lists)
        min_heap = []
        for i in range(n):
            if lists[i]:
                min_heap.append((lists[i].val, i, lists[i]))
        if not min_heap:
            return None
        heapq.heapify(min_heap)
        head = ListNode(None)
        curr = head
        while len(min_heap) > 0:
            _, i, top = heapq.heappop(min_heap)
            curr.next = top
            curr = curr.next
            if top.next:
                heapq.heappush(min_heap, (top.next.val, i, top.next))
        return head.next
