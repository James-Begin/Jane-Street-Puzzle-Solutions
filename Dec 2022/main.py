diffs = [24,99,136,224,240,
        24,90,108,179,139,224,
        42,117,247,90,155,
        105,71,45,261,99,280,
        144,153,509,252,314,
        193,40,162,252,135,167,
        9,355,95,135,781,
        12,21,361,145,128,225,
        18,27,601,152,215,
        5,44,66,194,108,168,
        77,45,371,66,115]


nums = [[57,33,132,268,492,732],
        [81,123,240,443,353,508],
        [186,42,195,704,452,228],
        [-7,2,357,452,317,395],
        [5,23,-4,592,445,620],
        [0,77,32,403,337,452]]
num2 = [[0,77,32,403,337,452],
        [5,23,-4,592,445,620],
        [-7,2,357,452,317,395],
        [186,42,195,704,452,228],
        [81,123,240,443,353,508],
        [57,33,132,268,492,732]]

vis = []

def search(nums, r, c, move, visited, count):
    # check if reached final space
    if r == len(nums) - 1 and c == len(nums[0]) - 1:
        return 0, visited
    print("check 1")
    #check if dice can move into spot based on move number and score
    if ((nums[r][c] - count) % move) != 0:# or nums[r][c] != score:
        return 0, visited
    print("check 2")
    if r >= len(nums) or r < 0 or c < 0 or c >= len(nums[0]):
        return 0, visited
    print("check 3")
    #get the value of the current space
    count = nums[r][c]
    #mark this space as visited
    visited.append((r,c))
    #recursively search in each direction
    count += search(nums, r + 1, c, move + 1, visited, count)[0]
    count += search(nums, r - 1, c, move + 1, visited, count)[0]
    count += search(nums, r, c + 1, move + 1, visited, count)[0]
    count += search(nums, r, c - 1, move + 1, visited, count)[0]

    return count, visited

ans = search(num2, 0, 0, 1, [], 0)

print(ans[0])
print(ans[1])






