def shuffle(nums):
    N = len(nums) - 1
    i = 0
    j = N
    result = []
    while j < len(nums):
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1
    return result


"""
Time Complexity => O(n)
Space Complexity => O(n)
"""
