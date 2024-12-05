def search_word(grid, word, row, col, direction):
    rows, cols = len(grid), len(grid[0])
    dr, dc = direction
    for i in range(len(word)):
        r, c = row + i * dr, col + i * dc
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != word[i]:
            return False
    return True

def main():
    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    word = "XMAS"
    num = 0
    matches = []
    directions = [
        (0, 1),   # r
        (0, -1),  # l
        (1, 0),   # d
        (-1, 0),  # u
        (1, 1),   # dr
        (-1, -1), # ul
        (1, -1),  # dl
        (-1, 1)   # ur
    ]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for direction in directions:
                if search_word(grid, word, row, col, direction):
                    matches.append((row, col, direction))

    for match in matches:
        num += 1

    print(num)

if __name__ == '__main__':
    main()
