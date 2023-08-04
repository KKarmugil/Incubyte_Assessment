class Spacecraft:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, command):
        if command == 'f':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif command == 'b':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
    def rotate(self, command):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        if command == 'l':
            new_index = (current_index - 1) % 4
        elif command == 'r':
            new_index = (current_index + 1) % 4
        self.direction = directions[new_index]
    def turn(self, command):
        if command == 'u':
            self.direction = 'Up'
        elif command == 'd':
            self.direction = 'Down'

    