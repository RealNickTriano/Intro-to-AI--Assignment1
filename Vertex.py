from unicodedata import name


class Vertex:

    # constructor
    def __init__(self, name, x_pos, y_pos, goal, start, h, g) -> None:
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.goal = goal
        self.start = start
        self.h_value = h
        self.g_value = g
        self.f_value = h + g