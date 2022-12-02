
with open('inputs/input1.txt', 'r') as f:
    input_cals = f.read().split('\n')
    max_cals, tmp_cal = [0, 0, 0], 0  # initialize
    for x in input_cals:
        if x == '':
            if not all(m > tmp_cal for m in max_cals):  # if greater than any of the current top 3
                max_cals[max_cals.index(min(max_cals))] = tmp_cal  # replace the min
            tmp_cal = 0
            continue
        else:
            tmp_cal = tmp_cal + int(x)
    print(f'Part 1: {max(max_cals)}')
    print(f'Part 2: {sum(max_cals)}')
