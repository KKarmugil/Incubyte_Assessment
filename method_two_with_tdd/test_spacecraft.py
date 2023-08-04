import unittest
from spacecraft_v2 import GalacticSpaceCraft

class TestSpaceCraft(unittest.TestCase):
    def test_initialization(self):
        craft = GalacticSpaceCraft(0, 0, 0, "N")
        self.assertEqual(craft.position, [0, 0, 0])
        self.assertEqual(craft.direction, "N")

    def test_move_forward(self):
        craft = GalacticSpaceCraft(0, 0, 0, "N")
        craft.move_forward()
        self.assertEqual(craft.position, [1, 0, 0])

    def test_move_backward(self):
        craft = GalacticSpaceCraft(1, 0, 0, "N")
        craft.move_backward()
        self.assertEqual(craft.position, [0, 0, 0])

    def test_turn_left(self):
        craft = GalacticSpaceCraft(0, 0, 0, "N")
        craft.turn_left()
        self.assertEqual(craft.direction, "W")

    def test_turn_right(self):
        craft = GalacticSpaceCraft(0, 0, 0, "N")
        craft.turn_right()
        self.assertEqual(craft.direction, "E")

    def test_turn_up(self):
        craft = GalacticSpaceCraft(0, 0, 0, "N")
        craft.turn_up()
        self.assertEqual(craft.direction, "Up")

    def test_turn_down(self):
        craft = GalacticSpaceCraft(0, 0, 0, "N")
        craft.turn_down()
        self.assertEqual(craft.direction, "Down")

def test_execute_commands(self):
    craft = GalacticSpaceCraft(0, 0, 0, "N")
    commands = ["f", "r", "u", "b", "l"]
    final_position, final_direction = craft.execute_commands(commands)
    self.assertEqual(final_position, [1, 0, -1])  # Fixed the expected position
    self.assertEqual(final_direction, "N")


if __name__ == "__main__":
    unittest.main()
