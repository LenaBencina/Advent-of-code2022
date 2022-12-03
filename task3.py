
def get_sum_priorities(part2=False):
    with open('inputs/input3.txt', 'r') as f:
        input_rucksacks = f.read().split('\n')
        total = 0
        n = 3 if part2 else 1
        for r_i in range(0, len(input_rucksacks) - (n - 1), n):  # for each n-th

            if part2:
                # for part2 take r_i-th, r_i+1-th, r_i+2-th rucksacks
                groups = [set(input_rucksacks[r_i]), set(input_rucksacks[r_i + 1]), set(input_rucksacks[r_i + 2])]
            else:
                # for part1 take t_i-th rucksack and slice it in half
                r = input_rucksacks[r_i]
                groups = set(r[:len(r) // 2]), set(r[len(r) // 2:])

            common = list(set.intersection(*groups))[0]  # get common element with set intersection
            priority = ord(common) - 38 if common.isupper() else ord(common) - 96  # get value from unicode code point
            total = total + priority

        print(f'Part {2 if part2 else 1}: {total}')


get_sum_priorities()
get_sum_priorities(part2=True)
