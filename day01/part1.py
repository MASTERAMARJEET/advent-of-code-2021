if __name__ == '__main__':
    input_file = 'day01/input.txt'
    depth_measure = 0
    with open(input_file, 'r') as f:
        previous = int(f.readline().removesuffix('\n'))
        for line in f:
            current = int(line.removesuffix('\n'))
            if current - previous > 0:
                depth_measure += 1
            previous = current
    print(f'The depth measure is {depth_measure}')
