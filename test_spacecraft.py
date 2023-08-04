import pytest
from spacecraft import Spacecraft

def test_spacecraft_initialization():
    spacecraft = Spacecraft((0, 0, 0), 'N')
    assert spacecraft.position == (0, 0, 0)
    assert spacecraft.direction == 'N'

def test_spacecraft_move_forward():
    spacecraft = Spacecraft((0, 0, 0), 'N')
    spacecraft.move('f')
    assert spacecraft.position == (1, 0, 0)

def test_spacecraft_move_backward():
    spacecraft = Spacecraft((1, 0, 0), 'N')
    spacecraft.move('b')
    assert spacecraft.position == (0, 0, 0)
