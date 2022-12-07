
with open('inputs/input7.txt', 'r') as f:
    output = f.read().split('\n')
    current_path = ['root']
    dir_sizes = {'root': 0}
    current_dir = 'root'
    for i in range(1, len(output)):
        line = output[i]
        if line == '$ ls':
            continue
        elif '$ cd' in line:
            current_dir = line.split('$ cd ')[1]
            if current_dir == '..':  # if move back
                current_dir = current_path.pop() # remove last dir from current path
            else:  # if moving to an actual dir
                current_path.append(current_dir)  # add to current path
                if current_dir not in dir_sizes:  # initialize size count for current dir
                    dir_sizes['/'.join(current_path)] = 0
        elif 'dir' in line:
            continue
        else:
            for j in range(len(current_path)):  # for each current and all previous dirs
                path = '/'.join(current_path[:j+1])
                dir_sizes[path] = dir_sizes[path] + int(line.split(' ')[0])  # increase dir size for file size

    # part 1
    total_size_dirs = sum([size for size in dir_sizes.values() if size <= 100000])
    print(total_size_dirs)

    # part 2
    to_delete = min([size for size in dir_sizes.values() if (70000000 - dir_sizes.get('root')) + size >= 30000000])
    print(to_delete)
