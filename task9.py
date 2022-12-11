
def move_head(h_pos, direction):
    h_pos_updated = h_pos.copy()
    if direction == 'R':
        h_pos_updated['x'] += 1
    if direction == 'L':
        h_pos_updated['x'] -= 1
    if direction == 'U':
        h_pos_updated['y'] += 1
    if direction == 'D':
        h_pos_updated['y'] -= 1
    return h_pos_updated


def move_tail(t_pos, h_pos, h_pos_updated):
    t_pos_updated = t_pos.copy()
    x_dist = abs(t_pos['x'] - h_pos_updated['x'])
    y_dist = abs(t_pos['y'] - h_pos_updated['y'])
    if x_dist == 2 or y_dist == 2:
        t_pos_updated = h_pos
    return t_pos_updated


with open('inputs/input9.txt', 'r') as f:
    motions = f.read().split('\n')
    h_pos, t_pos = {'x': 0, 'y': 0}, {'x': 0, 'y': 0}
    all_t_positions = set()
    for motion in motions:
        direction, num_moves = motion.split(' ')
        for move in range(int(num_moves)):
            # part 1
            # update
            h_pos_updated = move_head(h_pos, direction)
            t_pos_updated = move_tail(t_pos, h_pos, h_pos_updated)
            # save
            all_t_positions.add((t_pos_updated['x'], t_pos_updated['y']))
            # rewrite
            h_pos = h_pos_updated
            t_pos = t_pos_updated

    print(len(all_t_positions))
