# Intro to AI  Assignment1

# Authors

Nick Triano, Shayan Rahmatullah, Will Keleher

# How to Run

1) Install tkinter with pip install:
    pip install tk

2) Set FILE_PATH in main.py to graph a specific file

    Example: FILE_PATH = 'tests/test_0.txt'

3) Run in terminal with the following commands:

    To run A*:
        python3 main.py

    To run Theta*:
        python3 ThetaStar.py

# Notes
Control the display of the graph with the following constants.

If you use a smaller graph you may need to increase cell size to improve visibility

PADDING_X (padding from edges of canvas, affects whole graph)
PADDING_Y
SPACEING_X (spacing between nodes, increases cell  length/width)
SPACEING_Y
NODE_RADIUS (size of nodes)
LINEWIDTH (thickness of edges)

# Known Issues

1) For a 100x50 sized grid, the window size is bigger than a standard 1080p display
    The following values can be changed to be smaller, although it becomes hard to view:
    line 9 SPACEING_X
    line 10 SPACEING_Y 
    line 11 NODE_RADIUS 



 
