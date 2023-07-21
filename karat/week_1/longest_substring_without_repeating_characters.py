#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lengthOfLongestSubstring(self, s: str) -> int:
    lookup = set()
    left = right = 0
    length = 0

    while right < len(s):
        while s[right] in lookup:
            lookup.remove(s[left])
            left += 1
        length = max(length, right - left + 1)
        lookup.add(s[right])
        right += 1

    return length



""" 
Time Complexity -> O(n)
Space Complexity -> O(n)
"""











