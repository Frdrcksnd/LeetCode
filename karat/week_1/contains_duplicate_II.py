#https://leetcode.com/problems/contains-duplicate-ii/description/


def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    lookup = {}

    for idx, val in enumerate(nums):
        if val in lookup and idx - lookup[val] <= k:
            return True

        lookup[val] = idx

    return False


"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""