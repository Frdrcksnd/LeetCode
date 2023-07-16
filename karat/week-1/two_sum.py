#https://leetcode.com/problems/two-sum/

def twoSum(self, nums: List[int], target: int) -> List[int]:
    lookup = {}

    for idx, value in enumerate(nums):
        candidate = target - value

        if candidate in lookup:
            return [idx, lookup[candidate]]

        lookup[candidate] = idx

""" 
Time Complexity -> O(n)
Space Complexity -> O(n)
"""