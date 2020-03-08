import unittest
from segment import Segment


class TestSegment(unittest.TestCase):

    def test_move_OY_down(self):
        segment = Segment("", [10, 10], [0,0,0])
        segment.move_OY_down(5)
        self.assertEqual(segment.get_position_OY(), 15)

    def test_stop_at(self):
        segment = Segment("", [13, 37], [0, 0, 0])
        segment.stop_at(0)
        self.assertEqual(segment.get_position_OY(), 240)
