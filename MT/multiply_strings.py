"""https://leetcode.com/problems/multiply-strings/description/"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        lookup = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        first_num = 0
        second_num = 0
        for i in range(len(num1)):
            first_num *= 10
            first_num += lookup[num1[i]]

        for j in range(len(num2)):
            second_num *= 10
            second_num += lookup[num2[j]]
        result = first_num * second_num

        return str(result)
