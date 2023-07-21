#https://leetcode.com/problems/unique-morse-code-words/description/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        result = set()
        for word in words:
            code = ""
            for c in word:
                pos = ord(c) - 97
                code += lookup[pos]
            result.add(code)

        return len(result)

"""
Time Complexity -> O(NM) > N is number of words in array and M is length of longest word
Space Complexity -> O(n)
"""