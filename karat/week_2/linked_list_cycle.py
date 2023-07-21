#https://leetcode.com/problems/linked-list-cycle/

def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return True

"""
Time Complexity -> O(n)
Space Complexity -> O(1)
"""