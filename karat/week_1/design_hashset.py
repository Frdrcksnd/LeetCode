#https://leetcode.com/problems/design-hashset/description/


class MyHashSet:

    def __init__(self):
        self.map = {}

    def add(self, key: int) -> None:
        self.map[key] = key

    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]

    def contains(self, key: int) -> bool:
        if key in self.map:
            return True
        return False


"""
Time Complexity -> O(1)
Space Complexity -> O(n)
"""