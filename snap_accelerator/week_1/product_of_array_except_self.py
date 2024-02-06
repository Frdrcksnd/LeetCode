def productExceptSelf(nums):
    N = len(nums)
    left = [0] * N
    right = [0] * N
    answer = [0] * N

    for i in range(N):

        if i == 0:
            left[i] = nums[i]
        else:
            left[i] = left[i - 1] * nums[i]

    for j in reversed(range(N)):
        if j == N - 1:
            right[j] = nums[j]
        else:
            right[j] = right[j + 1] * nums[j]

    for i in range(N):
        if i == 0:
            answer[i] = right[i + 1]
        elif i == N - 1:
            answer[i] = left[i - 1]
        else:
            answer[i] = left[i - 1] * right[i + 1]
    return answer


"""
Time Complexity => O(n)
Space Complexity => O(n)
"""
