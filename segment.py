from sprite import Sprite


class Segment(Sprite):

    def move_OY_down(self, delta_pos: int):
        self._position[1] = self._position[1] + delta_pos
        if self._position[1] > 357:
            self._position[1] = -240

    def stop_at(self, symbol_number: int):
        if symbol_number == 0:
            self._position[1] = 240
        elif symbol_number == 1:
            self._position[1] = 137
        elif symbol_number == 2:
            self._position[1] = 35
        elif symbol_number == 3:
            self._position[1] = -70
        elif symbol_number == 4:
            self._position[1] = -172
