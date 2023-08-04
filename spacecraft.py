class Spacecraft:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, command):
        if command == 'f':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif command == 'b':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
