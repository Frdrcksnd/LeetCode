"""https://leetcode.com/problems/next-permutation/"""

def next_permutation(nums):
    right = 0 # index to right of pivot

    for i in reversed(range(len(nums))):
        if nums[i-1] < nums[i]:
            right = i
            break
    if right == 0:
        nums.sort()
        return nums
    pivot = right - 1
    for i in reversed(range(len(nums))):
        if nums[i] > nums[pivot]:
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break
    nums[right:] = sorted(nums[right:])