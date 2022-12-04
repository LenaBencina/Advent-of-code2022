# option 1
def get_total_overlaps(part):
    op_dict = {1: lambda x, y: x & y, 2: lambda x, y: x | y}
    with open('inputs/input4.txt', 'r') as f:
        input_asgmnts = f.read().split('\n')
        total = 0
        for pair in input_asgmnts:
            # prepare min, max for both intervals
            p1, p2 = pair.split(',')
            p1_min, p1_max = map(int, p1.split('-'))
            p2_min, p2_max = map(int, p2.split('-'))
            # check if satisfied the condition of containing/overlapping
            is_in1 = op_dict.get(part)((p2_min >= p1_min) & (p2_min <= p1_max), (p2_max >= p1_min) & (p2_max <= p1_max))
            is_in2 = op_dict.get(part)((p1_min >= p2_min) & (p1_min <= p2_max), (p1_max >= p2_min) & (p1_max <= p2_max))
            total = total + min(1, is_in1 + is_in2)  # or + max(is_in1, is_in2)

        print(f'Part {part}: {total}')


# get_total_overlaps(part=1)
# get_total_overlaps(part=2)


# option2
def get_total_overlaps2(part):
    with open('inputs/input4.txt', 'r') as f:
        min_max_index = 0 if part == 2 else 1
        input_asgmnts = f.read().split('\n')
        total = 0
        for pair in input_asgmnts:
            # prepare intervals
            p1, p2 = pair.split(',')
            p1, p2 = list(map(int, p1.split('-'))), list(map(int, p2.split('-')))
            # check if satisfied the condition of containing/overlapping
            is_in = (p2[0] >= p1[0]) & (p2[min_max_index] <= p1[1]) | (p1[0] >= p2[0]) & (p1[min_max_index] <= p2[1])
            total = total + is_in
        print(f'Part {part}: {total}')


get_total_overlaps2(part=1)
get_total_overlaps2(part=2)
