
with open('inputs/input8.txt', 'r') as f:
    grid = f.read().split('\n')
    count_total = 0  # for part1
    max_score = 0  # for part2
    grid_size = len(grid)  # square grid

    # loop through (x, y) coordinates for inner trees
    for x in range(1, grid_size - 1):
        for y in range(1, grid_size - 1):
            candidate = int(grid[y][x])
            # for part1
            counts = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
            # for part2
            dist = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
            visibility = {'up': True, 'down': True, 'left': True, 'right': True}

            # left (same y)
            for x_l in range(x - 1, 0 - 1, -1):
                neighbour = int(grid[y][x_l])
                counts['left'] += int(neighbour < candidate)  # add 1 or 0
                dist['left'] += int(visibility['left'])  # add 1 or 0
                if neighbour >= candidate:  # first time the view is blocked switch to false
                    visibility['left'] = False

            # right (same y)
            for x_r in range(x + 1, grid_size):
                neighbour = int(grid[y][x_r])
                counts['right'] += int(neighbour < candidate)
                dist['right'] += int(visibility['right'])
                if neighbour >= candidate:
                    visibility['right'] = False

            # up (same x)
            for y_u in range(y - 1, 0 - 1, -1):
                neighbour = int(grid[y_u][x])
                counts['up'] += int(neighbour < candidate)
                dist['up'] += int(visibility['up'])
                if neighbour >= candidate:
                    visibility['up'] = False

            # down (same x)
            for y_d in range(y + 1, grid_size):
                neighbour = int(grid[y_d][x])
                counts['down'] += int(neighbour < candidate)
                dist['down'] += int(visibility['down'])
                if neighbour >= candidate:
                    visibility['down'] = False

            # part1; add 1 if at least one way is visible
            up = counts['up'] == y
            down = counts['down'] == grid_size - 1 - y
            left = counts['left'] == x
            right = counts['right'] == grid_size - 1 - x
            if up or down or left or right:
                count_total = count_total + 1

            # part 2; multiply and check if larger than current max
            tmp_score = dist['up'] * dist['down'] * dist['left'] * dist['right']
            max_score = tmp_score if tmp_score > max_score else max_score

    count_visible = count_total + (4 * len(grid) - 4)  # add all edge trees
    print(f'Number of visible trees: {count_visible}')

    # part2
    print(f'Max score: {max_score}')
