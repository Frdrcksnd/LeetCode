#https://leetcode.com/problems/valid-parentheses/


class Solution:
    def check(self, opening, closing):
        if opening == "(" and closing == ")":
            return True
        elif opening == "[" and closing == "]":
            return True
        elif opening == "{" and closing == "}":
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        s = list(s)




"""
Time Complexity -> O(1)
Space Complexity -> O(n)
"""