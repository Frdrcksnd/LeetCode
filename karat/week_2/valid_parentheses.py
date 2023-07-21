#https://leetcode.com/problems/valid-parentheses/


class Solution:

    def isValid(self, s: str) -> bool:
        lookup = {"]": "[", ")": "(", "}": "{"}

        stack = []

        for c in s:
            if c not in lookup:
                stack.append(c)
            elif stack and stack[-1] == lookup[c]:
                stack.pop()
            else:
                return False

        return not stack


"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""







"""
Time Complexity -> O(1)
Space Complexity -> O(n)
"""