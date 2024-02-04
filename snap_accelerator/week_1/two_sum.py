
def two_sum(self, nums: List[int], target: int) -> List[int]:
    lookup = {}

    for idx, num in enumerate(nums):
        val = target - num
        if val in lookup and lookup[val] != idx:
            return [idx, lookup[val]]
        lookup[num] = idx

"""
Time Complexity => O(n)
Space Complexity => O(n)
"""