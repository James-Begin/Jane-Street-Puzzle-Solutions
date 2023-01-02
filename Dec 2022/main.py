grid = [[57,33,132,268,492,732],
        [81,123,240,443,353,508],
        [186,42,195,704,452,228],
        [-7,2,357,452,317,395],
        [5,23,-4,592,445,620],
        [0,77,32,403,337,452]]
def solve(grid, pos, score, visited, dice):
    # base case: if the die has reached the lower-right corner, return the sum of the values in the unvisited squares
    if pos == (0, 5):
        ans = 0
        for (i, j) in visited:
            print(i,j)
            grid[i][j] = 0
        for j in grid:
            ans += sum(j)
        return ans

    # try to move the die to each of the adjacent squares
    for di, dj in [(1, 0), (-1, 0), (0 , 1), (0, -1)]:
        i, j = pos
        i2, j2 = i + di, j + dj
        if not (0 <= i2 < 6 and 0 <= j2 < 6):
            continue  # square is out of bounds

        num = ((grid[i2][j2] - score) // (len(visited)+1))
        score2 = score + (num) * (len(visited)+1)

        print(dice)
        if score2 == grid[i2][j2]:
            if (num) not in dice and len(dice) > 6:
                continue
            else:
                dice.add(num)
            visited.append((i2, j2))
            print(f"Moving from {pos} to {(i2, j2)} with score {score2}")  # print the path taken
            print(f'Visited: {visited}')

            result = solve(grid, (i2, j2), score2, visited, dice)
            visited.remove((i2, j2))
            if num in dice:
                dice.remove(num)
            if result is not None:
                return result
    # no valid moves were found
    return None


# start the recursion from the upper-left corner with a score of 0
result = solve(grid, (5, 0), 0, [], set())
print(result)
