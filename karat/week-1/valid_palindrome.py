#https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False

    return True


"""
Time Complexity -> O(n)
Space Complexity -> O(1)
"""