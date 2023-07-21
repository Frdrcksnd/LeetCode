#https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lookup = set()

        while headA:
            lookup.add(headA)
            headA = headA.next

        while headB:
            if headB in lookup:
                return headB
            headB = headB.next

        return None


"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""