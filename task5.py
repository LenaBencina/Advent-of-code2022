def get_rearrangement(part):
    with open('inputs/input5.txt', 'r') as f:
        stacks, steps = f.read().split('\n\n')
        stacks, steps = stacks.split('\n'), steps.split('\n')

        # prepare rows in list
        rows = [row.replace('    ', '*').replace(' ', '').replace('[', '').replace(']', '') for row in stacks[:-1]]

        # convert to columns
        n = int(stacks[-1].replace(' ', '')[-1])  # get number of stacks
        columns = [[] for x in range(n)]  # prepare list of n empty lists
        for row in rows:
            for i in range(len(row)):  # for each crate
                if row[i] != '*':  # add only if not empty (i.e. *)
                    columns[i].append(row[i])

        # start moving crates: for each step
        for step_str in steps:
            # prepare instructions dict from string
            step_list = step_str.split(' ')
            step_dict = {step_list[i]: int(step_list[i+1]) for i in range(0, len(step_list) - 1, 2)}

            if part == 1:
                for i in range(1, step_dict.get('move') + 1):  # for each move within one step/instruction
                    column_to = columns[step_dict.get('to') - 1]  # where to move
                    moving_crate = columns[step_dict.get('from') - 1].pop(0)  # parse crate needed to be moved
                    column_to[:0] = moving_crate  # add one crate to beginning of the stack

            if part == 2:
                column_to = columns[step_dict.get('to') - 1]  # where to move
                # parse crate needed to be moved
                moving_crates = [columns[step_dict.get('from') - 1].pop(0) for i in range(1, step_dict.get('move') + 1)]
                column_to[:0] = moving_crates  # add multiple crates to beginning of the stack

        print(f'Part {part}: {"".join([col[0] for col in columns])}')


get_rearrangement(part=1)
get_rearrangement(part=2)
