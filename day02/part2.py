class Position:

    def __init__(self) -> None:
        self.aim = 0
        self.cordinates = [0,0]

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Position):
            return NotImplemented
        return self.cordinates[0] == __o.cordinates[0] & self.cordinates[0] == __o.cordinates[0]

    def __repr__(self) -> str:
        return f"horizontal: {self.horizontal}, depth: {self.depth}"

    @property
    def horizontal(self) -> int:
        return self.cordinates[0]

    @property
    def depth(self) -> int:
        return self.cordinates[1]

    def move_forward(self, distance: int) -> None:
        self.cordinates[0] += distance
        self.cordinates[1] += self.aim*distance

    def move_down(self, distance: int) -> None:
        self.aim += distance

    def move_up(self, distance: int) -> None:
        self.aim -= distance


if __name__ == '__main__':
    input_file = 'day02/input.txt'
    submarine = Position()
    with open(input_file, 'r') as f:
        for line in f:
            direction, distance = line.removesuffix('\n').split(' ')
            if (direction == 'forward'):
                submarine.move_forward(int(distance))
            elif (direction == 'down'):
                submarine.move_down(int(distance))
            elif (direction == 'up'):
                submarine.move_up(int(distance))
    print(f'The horizontal position is {submarine.horizontal} and the depth is {submarine.depth}')
    print(f'The required answer is {submarine.horizontal*submarine.depth}')

