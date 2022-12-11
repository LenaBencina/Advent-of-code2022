
with open('inputs/input10.txt', 'r') as f:
    instructions = f.read().split('\n')
    x = 1
    cycle_number = 1
    instruction_number = 0
    result_sum = 0
    execute = False

    # loop trough instructions
    while instruction_number < len(instructions):

        instruction = instructions[instruction_number][:4]

        if cycle_number in [20, 60, 100, 140, 180, 220]:
            result_sum += (cycle_number * x)

        if instruction == 'noop':
            instruction_number += 1
        else:
            if execute:  # execute but not read! we need the variable from previous cycle
                x += int(value_to_add)
                execute = False
                instruction_number += 1
            else:  # read only
                execute = True
                value_to_add = instructions[instruction_number].split(' ')[1]

        # increase cycle in each loop
        cycle_number += 1

    print(result_sum)
