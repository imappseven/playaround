# Solution 1
# def minFallingPathSum(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: int
#     """
    
#     min_sum = [float('inf')]

#     for col in range(len(matrix[0])):
#         count_sum(matrix, 0, col, 0, min_sum)

#     return min_sum[0]

# def count_sum(matrix, row, col, sum, min_sum):
#     if row == len(matrix) - 1:
#         min_sum[0] = min(min_sum[0], sum + matrix[row][col])
#         return

#     next_pos = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

#     for next_row, next_col in next_pos:
#         if 0 <= next_row < len(matrix) and next_col >= 0  and next_col < len(matrix[0]):
#             count_sum(matrix, next_row, next_col, sum + matrix[row][col], min_sum)

def minFallingPathSum(matrix):
    min_sum = float('inf')
    memo = {}

    for col in range(len(matrix[0])):
        min_sum = min(min_sum, count_paths(matrix, 0, col, memo))

    return min_sum

def count_paths(matrix, row, col, memo):
    if row == len(matrix) - 1:
        return matrix[row][col]

    if (row, col) in memo:
        return memo[(row, col)]

    next_positions = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    min_sum = float('inf')

    for next_row, next_col in next_positions:
        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):
            path_sum = matrix[row][col] + count_paths(matrix, next_row, next_col, memo)
            min_sum = min(min_sum, path_sum)

    memo[(row, col)] = min_sum
    return min_sum





print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(minFallingPathSum([[-19,57],[-40,-5]]))