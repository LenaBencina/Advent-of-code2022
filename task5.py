
def get_rearrangement(part):
    with open('inputs/input5.txt', 'r') as f:
        stacks_tmp, steps = f.read().split('\n\n')
        stacks_tmp, steps = stacks_tmp.split('\n'), steps.split('\n')

        n = int(stacks_tmp[-1].replace(' ', '')[-1])

        # prepare rows in list
        rows = [row.replace('    ', '*').replace(' ', '').replace('[', '').replace(']', '') for row in stacks_tmp[:-1]]

        # convert to columns
        columns = [[] for x in range(n)]
        for row in rows:
            position = 0
            for col_i in row:
                columns[position].append(col_i)
                position = position + 1

        # remove empty places (*)
        columns = [[y for y in x if y != '*'] for x in columns]

        # for each step
        for step_str in steps:
            step_dict = dict(zip(['amount', 'from', 'to'], [int(s) for s in step_str.split() if s.isdigit()]))

            if part == 1:
                for i in range(1, step_dict.get('amount') + 1):
                    column_to_index = step_dict.get('to') - 1
                    column_to = columns[column_to_index]
                    moving_crate = columns[step_dict.get('from') - 1].pop(0)
                    if moving_crate == '*':
                        continue
                    column_to.insert(0, moving_crate)

            if part == 2:
                column_to_index = step_dict.get('to') - 1
                column_to = columns[column_to_index]
                moving_crates = [columns[step_dict.get('from') - 1].pop(0) for i in range(1, step_dict.get('amount') + 1)]
                column_to[:0] = moving_crates

        print(f'Part {part}: {"".join([col[0] for col in columns])}')


get_rearrangement(part=1)
get_rearrangement(part=2)
