#https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cache = []

        curr = head

        while curr:
            cache.append(curr.val)
            curr = curr.next
        return cache == cache[::-1]

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        cache = []

        curr = head

        while curr:
            cache.append(curr.val)
            curr = curr.next
        left = 0
        right = len(cache) - 1

        while left < right:
            if cache[left] != cache[right]:
                return False
            left += 1
            right -= 1
        return False

"""
Time Complexity -> O(1)
Space Complexity -> O(n)
"""

# ********************** Constant Space Solution ******************************

""" 
Constant space algorithm :

- break list into 2 halve
- reverse second half
- compare both halves
- combine list
- return result
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = head
        second = self.reverse(self.split(head))
        one, two = first, second
        result = True
        while one and two:
            if one.val != two.val:
                result = False
            one = one.next
            two = two.next
        first.next = self.reverse(second)
        return result

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next

            curr.next = prev
            prev = curr

            curr = next_node
        return prev

    def split(self, head):
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next


"""
Time Complexity -> O(1)
Space Complexity -> O(1)
"""