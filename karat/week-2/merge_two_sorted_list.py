#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional
        sentinel = ListNode()
        curr = sentinel

        first = list1
        second = list2

        while first and second:
            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next

        curr.next = first or second

        return sentinel.next



"""
Time Complexity -> O(n)
Space Complexity -> O(1)
"""