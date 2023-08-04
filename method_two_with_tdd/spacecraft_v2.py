
class GalacticSpaceCraft:
    def __init__(self, x, y, z, direction):
        self.position = [x, y, z]
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.position[0] += 1
        elif self.direction == "S":
            self.position[0] -= 1
        elif self.direction == "E":
            self.position[1] += 1
        elif self.direction == "W":
            self.position[1] -= 1
        elif self.direction == "Up":
            self.position[2] += 1
        elif self.direction == "Down":
            self.position[2] -= 1

    def move_backward(self):
        if self.direction == "N":
            self.position[0] -= 1
        elif self.direction == "S":
            self.position[0] += 1
        elif self.direction == "E":
            self.position[1] -= 1
        elif self.direction == "W":
            self.position[1] += 1
        elif self.direction == "Up":
            self.position[2] -= 1
        elif self.direction == "Down":
            self.position[2] += 1

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"

    def turn_up(self):
        if self.direction == "N":
            self.direction = "Up"
        elif self.direction == "S":
            self.direction = "Down"
        elif self.direction == "E" or self.direction == "W":
            # No change in horizontal direction
            pass

    def turn_down(self):
        if self.direction == "N":
            self.direction = "Down"
        elif self.direction == "S":
            self.direction = "Up"
        elif self.direction == "E" or self.direction == "W":
            # No change in horizontal direction
            pass

    def execute_commands(self, commands):
        for cmd in commands:
            if cmd == "f":
                self.move_forward()
            elif cmd == "b":
                self.move_backward()
            elif cmd == "l":
                self.turn_left()
            elif cmd == "r":
                self.turn_right()
            elif cmd == "u":
                self.turn_up()
            elif cmd == "d":
                self.turn_down()

        return self.position, self.direction
