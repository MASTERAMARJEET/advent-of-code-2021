def parse_line(line):
    return int(line.removesuffix('\n'))

if __name__ == '__main__':
    input_file = 'input.txt'
    depth_measure = 0
    with open(input_file, 'r') as f:
        a, b, c = parse_line(f.readline()),parse_line(f.readline()),parse_line(f.readline())
        previous_window = sum([a,b,c])
        for line in f:
            a, b, c = b, c, parse_line(line)
            current_window = sum([a,b,c])
            if current_window - previous_window > 0:
                depth_measure += 1
            previous_window = current_window
    print(f'The depth measure is {depth_measure}')
