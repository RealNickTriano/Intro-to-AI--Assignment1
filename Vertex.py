class Vertex:

    # constructor
    def __init__(self, name, x_pos, y_pos, goal, start, h, g, parent = None) -> None:
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.goal = goal
        self.start = start
        self.h_value = h
        self.g_value = g
        self.f_value = h + g
        self.parent = parent

    """ def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Vertex) and __o.name == self.name """
    
    def __lt__(self, __o: object) -> bool:
        return isinstance(__o, Vertex) and __o.name < self.name
    
    def updateFValue(self):
        self.f_value = self.g_value + self.h_value
