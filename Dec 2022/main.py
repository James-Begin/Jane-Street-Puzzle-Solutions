import sys

sys.setrecursionlimit(10000)

# diffs = [24,99,136,224,240,
#         24,90,108,179,139,224,
#         42,117,247,90,155,
#         105,71,45,261,99,280,
#         144,153,509,252,314,
#         193,40,162,252,135,167,
#         9,355,95,135,781,
#         12,21,361,145,128,225,
#         18,27,601,152,215,
#         5,44,66,194,108,168,
#         77,45,371,66,115]
#
#
# nums = [[57,33,132,268,492,732],
#         [81,123,240,443,353,508],
#         [186,42,195,704,452,228],
#         [-7,2,357,452,317,395],
#         [5,23,-4,592,445,620],
#         [0,77,32,403,337,452]]
# num2 = [[0,77,32,403,337,452],
#         [5,23,-4,592,445,620],
#         [-7,2,357,452,317,395],
#         [186,42,195,704,452,228],
#         [81,123,240,443,353,508],
#         [57,33,132,268,492,732]]
#
# vis = []
#
# def search(nums, r, c, move, visited, count):
#     # check if reached final space
#     if r == len(nums) - 1 and c == len(nums[0]) - 1:
#         return 0, visited
#     print("check 1")
#     #check if dice can move into spot based on move number and score
#     if ((nums[r][c] - count) % move) != 0:
#         return 0, visited
#     print("check 2")
#     if r >= len(nums) or r < 0 or c < 0 or c >= len(nums[0]):
#         return 0, visited
#     print("check 3")
#     #get the value of the current space
#     count = nums[r][c]
#     #mark this space as visited
#     visited.append((r,c))
#     #recursively search in each direction
#     count += search(nums, r + 1, c, move + 1, visited, count)[0]
#     count += search(nums, r - 1, c, move + 1, visited, count)[0]
#     count += search(nums, r, c + 1, move + 1, visited, count)[0]
#     count += search(nums, r, c - 1, move + 1, visited, count)[0]
#
#     return count, visited
#
# ans = search(num2, 0, 0, 1, [], 0)
#
# print(ans[0])
# print(ans[1])
#


'''
def solve(grid):
  # Set up variables to keep track of the path and visited squares
  path = []
  visited = set()
  visited_squares = []

  # Set up a list of possible moves
  moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  # Start at the lower-left corner of the grid
  current_square = (0, 0)
  score = 0

  # Explore paths until we reach the upper-right corner or run out of paths
  while current_square != (5, 5):
    # Check if the score matches the value in the current square
    if score == grid[current_square[0]][current_square[1]]:
      # Mark the current square as visited
      visited.add(current_square)
      visited_squares.append(current_square)

      # Explore the possible moves from the current square
      for move in moves:
        next_square = (current_square[0] + move[0], current_square[1] + move[1])
        if is_valid_move(next_square, grid, visited):
          # Update the score and push the new square onto the stack
          score += (len(path) + 1) * grid[next_square[0]][next_square[1]]
          path.append(next_square)
          break
    else:
      # Continue exploring other paths by continuing the inner loop
      continue

  # Sum up the values in the unvisited squares
  unvisited_sum = 0
  for i in range(6):
    for j in range(6):
      if (i, j) not in visited:
        unvisited_sum += grid[i][j]

  return visited_squares, unvisited_sum

def is_valid_move(square, grid, visited):
  # Check if the square is within the bounds of the grid
  if square[0] < 0 or square[0] >= 6 or square[1] < 0 or square[1] >= 6:
    return False
  # Check if the square has already been visited
  if square in visited:
    return False
  return True
'''
# Test the solution with the given grid
grid = [[57,33,132,268,492,732],
[81,123,240,443,353,508],
[186,42,195,704,452,228],
[-7,2,357,452,317,395],
[5,23,-4,592,445,620],
[0,77,32,403,337,452]]
'''
visited_squares, unvisited_sum = solve(grid)
print(visited_squares)  # Prints the list of visited squares
print(unvisited_sum)'''


'''def solve(grid, row, col, score, visited):
    # base case: we have reached the upper-right corner
    if row == 0 and col == len(grid[0]) - 1:
        return sum([grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) if not visited[i][j]])

    # try moving up
    if row > 0 and not visited[row - 1][col] and score + (row + 1) * (col + 1) == grid[row - 1][col]:
        visited[row][col] = True
        result = solve(grid, row - 1, col, score + (row + 1) * (col + 1), visited)
        visited[row][col] = False
        if result is not None:
            return result

    # try moving down
    if row < len(grid) - 1 and not visited[row + 1][col] and score + (row + 1) * (col + 1) == grid[row + 1][col]:
        visited[row][col] = True
        result = solve(grid, row + 1, col, score + (row + 1) * (col + 1), visited)
        visited[row][col] = False
        if result is not None:
            return result

    # try moving left
    if col > 0 and not visited[row][col - 1] and score + (row + 1) * (col + 1) == grid[row][col - 1]:
        visited[row][col] = True
        result = solve(grid, row, col - 1, score + (row + 1) * (col + 1), visited)
        visited[row][col] = False
        if result is not None:
            return result

    # try moving right
    if col < len(grid[0]) - 1 and not visited[row][col + 1] and score + (row + 1) * (col + 1) == grid[row][col + 1]:
        visited[row][col] = True
        result = solve(grid, row, col + 1, score + (row + 1) * (col + 1), visited)
        visited[row][col] = False
        if result is not None:
            return result

    # no valid moves, return None
    return None


# initialize visited array
visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

# start at lower-left corner with score 0
result = solve(grid, len(grid) - 1, 0, 0, visited)
print(result)
'''

'''
def combinationSum(arr, sum):
    ans = []
    temp = []

    # first do hashing nothing but set{}
    # since set does not always sort
    # removing the duplicates using Set and
    # Sorting the List
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans


def findNumbers(ans, arr, temp, sum, index):
    if (sum == 0):
        # Adding deep copy of list to ans
        ans.append(list(temp))
        return

    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):

        # checking that sum does not become negative
        if (sum - arr[i]) >= 0:
            # adding element which can contribute to
            # sum
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum - arr[i], i)

            # removing element from list (backtracking)
            temp.remove(arr[i])


# Driver Code
arr = [57,33,132,268,492,732,
81,123,240,443,353,508,
186,42,195,704,452,228,
-7,2,357,452,317,395,
5,23,-4,592,445,620,
0,77,32,403,337,452]
sum = 5549
ans = combinationSum(arr, sum)

# If result is empty, then
if len(ans) <= 0:
    print("empty")

# print all combinations stored in ans
for i in range(len(ans)):

    print("(", end=' ')
    for j in range(len(ans[i])):
        print(str(ans[i][j]) + " ", end=' ')
    print(")", end=' ')'''
''''''
from typing import List


def solve(grid: List[List[int]]) -> int:
    # initialize the dp array
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(1, len(grid)):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, len(grid[0])):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # fill in the rest of the dp array
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):

            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j + 1]) + grid[i][j]



    # add up the values in the unvisited squares
    result = 0
    ans = []
    print(dp)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dp[i][j] > dp[len(grid) - 1][len(grid[0]) - 1]:
                result += grid[i][j]
                ans.append(grid[i][j])
    return result, ans

grid = [[57,33,132,268,492,732],
        [81,123,240,443,353,508],
        [186,42,195,704,452,228],
        [-7,2,357,452,317,395],
        [5,23,-4,592,445,620],
        [0,77,32,403,337,452]]

result, ans = solve(grid)
print(result)
print(ans)
print(sum(ans))

total = 0
for i in grid:
    for j in i:
        total += j
print(total)

for m in range(len(grid)-1):
    for l in range(len(grid[0])-1):
        if grid[m][l] in ans:
            grid[m][l] = -1


print(grid)


