#https://leetcode.com/problems/reshape-the-matrix/description/


def flatten_list(self, nums):
    result = []
    for arr in nums:
        for num in arr:
            result.append(num)
    return result



def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    row = len(mat)
    col = len(mat[0])
    if row * col != r * c:
        return mat
    flattened_matrix = flatten_list(mat)
    output = [[0 for _ in range(c)] for _ in range(r)]

    k = 0

    for i in range(r):
        for j in range(c):
            output[i][j] = flattened_matrix[k]
            k += 1
    return output



"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""