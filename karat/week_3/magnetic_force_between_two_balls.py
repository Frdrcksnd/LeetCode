#https://leetcode.com/problems/magnetic-force-between-two-balls/description/

class Solution:

    def calculate_distance(self, distance, position):
        curr = position[0]
        balls = 1

        for i in range(1, len(position)):
            if position[i] - curr >= distance:
                curr = position[i]
                balls += 1
        return balls

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        left = 0
        right = position[-1] - position[0]

        while left <= right:
            mid = (left + right)//2

            if self.calculate_distance(mid, position) >= m:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


"""
Time Complexity -> O(nlogn)
Space Complexity -> O(1)
"""