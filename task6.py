
def get_char_number(n):
    with open('inputs/input6.txt', 'r') as f:
        buffer = f.read()
        for i in range(len(buffer) - n):  # loop through characters
            if len(set(buffer[i:i + n])) == len(buffer[i:i + n]):  # if current n characters are unique
                print(f'n={n}: {i + n}')  # return the first position after n unique characters
                return


get_char_number(n=4)
get_char_number(n=14)
