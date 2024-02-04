def shuffle(nums)
    i = 0
    j = n
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