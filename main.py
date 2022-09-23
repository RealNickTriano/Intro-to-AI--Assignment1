import math
from textwrap import fill
from Vertex import Vertex
from tkinter import *


PADDING_X = 50
PADDING_Y = 50
SPACEING_X = 50
SPACEING_Y = 50
NODE_RADIUS = 10
LINEWIDTH = 2

FILE_PATH = 'demo.txt'

root = Tk()
root.title('Codemy.com -  Canvas')
root.geometry("1920x1080")

my_canvas = Canvas(root, width=1920, height=1080, bg="white")
my_canvas.pack(pady=20)
vertices = []

# --------- Create labels ---------------

lbl_x_value = Label(my_canvas, bg='white', font=('Arial', 16), text='x: ')
lbl_y_value = Label(my_canvas, bg='white', font=('Arial', 16), text='y: ')
lbl_goal = Label(my_canvas, bg='white', font=('Arial', 16), text='goal: ')
lbl_start = Label(my_canvas, bg='white', font=('Arial', 16), text='start: ')
lbl_h_value = Label(my_canvas, bg='white', font=('Arial', 16), text='h: ')
lbl_g_value = Label(my_canvas, bg='white', font=('Arial', 16), text='g: ')
lbl_f_value = Label(my_canvas, bg='white', font=('Arial', 16), text='f: ')
lbl_x_value.place(relx=0.1, rely=0.95, anchor='center')
lbl_y_value.place(relx=0.2, rely=0.95, anchor='center')
lbl_goal.place(relx=0.3, rely=0.95, anchor='center')
lbl_start.place(relx=0.4, rely=0.95, anchor='center')
lbl_h_value.place(relx=0.5, rely=0.95, anchor='center')
lbl_g_value.place(relx=0.6, rely=0.95, anchor='center')
lbl_f_value.place(relx=0.7, rely=0.95, anchor='center')

# --------- End Create labels ---------------

def updateLabels(v):
    lbl_x_value.config(text= 'x: ' + str(v.x_pos))
    lbl_y_value.config(text= 'y: ' + str(v.y_pos))
    lbl_goal.config(text= 'goal: ' + str(v.goal))
    lbl_start.config(text= 'start: ' + str(v.start))
    lbl_h_value.config(text= 'h: ' + str(v.h_value))
    lbl_g_value.config(text= 'g: ' + str(v.g_value))
    lbl_f_value.config(text= 'f: ' + str(v.f_value))

def handle_enter_vertex(event):
    # find the canvas item below mouse cursor
    item = my_canvas.find_withtag("current")
    # now we can get this vertex from our stored array of vertices
    # and check anything we want!
    updateLabels(vertices[item[0] - 1])

def handle_leave_vertex(event):
    # clear the label text
    pass

# TODO: Refactor to use data from input file

#Types: int m, int n, Array[Tuple(x,y,z)]: 
def create_adj_matrix(m, n, cells):
    matrix = []
    
    for i in range(0, (m + 1) * (n + 1)):
        row = []
        for j in range(0, (m + 1) * (n + 1)):
                row.append(0)
        matrix.append(row)
    
    # matrix is init with all 0's

    for item in cells:
        print(item)
        x = item[0] - 1 
        y = item[1] - 1
        blocked = item[2]
        # Find vertex id from (x, y)
        vid = y * (m + 1) + x
        print(vid)
        if not blocked:
            matrix[vid][vid + 1] = 1
            matrix[vid][vid + m + 1] = 1
            matrix[vid][vid + m + 2] = 1
            matrix[vid + m + 1][vid + m + 2] = 1
            matrix[vid + 1][vid + m + 1] = 1
            matrix[vid + 1][vid + m + 2] = 1
        else:
            pass

    return matrix

# TODO
def getVertexid(tuple):
    id = 0
    (1,1)
    return id

def getVertexCoords(vid):
    vTuple = ()

    return vTuple
# Arguments: x pos, y pos, r radius, goal bool, start bool
def create_circle(x, y, r, canvas, goal, start): # center x,y, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    if goal and start:
        c = canvas.create_oval(x0, y0, x1, y1, fill='purple')
    elif goal:
        c = canvas.create_oval(x0, y0, x1, y1, fill='blue')
    elif start:
        c = canvas.create_oval(x0, y0, x1, y1, fill='red')
    else:
        c = canvas.create_oval(x0, y0, x1, y1, fill='#000')
    canvas.tag_bind(c, "<Enter>", handle_enter_vertex)
    canvas.tag_bind(c, "<Leave>", handle_leave_vertex)
    # Hold vertex in array
    v = Vertex(c, x, y, goal, start, 0, 0)
    vertices.append(v)

    return c

# From adjacency matrix draw the graph O(n^2)
def display_grid(matrix, m, n, goal_pos, start_pos): # n = dim of matrix n * n
    for i in range(0, (n + 1)):
        for j in range(0, (m + 1)):
            goal = False
            start = False
            if (j + 1, i + 1) == goal_pos:
                goal = True
            if (j + 1, i + 1) == start_pos:
                start = True
            create_circle(j * SPACEING_X + PADDING_X, i * SPACEING_Y + PADDING_Y, NODE_RADIUS,  my_canvas, goal, start)   
            
    for k in range(0, (m + 1) * (n + 1)):
        for q in range(k, (m + 1) * (n + 1)):
            if(matrix[k][q] == 1):
                mytag = "({},{})".format(k,q)
                # draw line from vertex i to vertex j
                my_canvas.create_line((k % 5) * SPACEING_X + PADDING_X, 
                                    math.floor(k / 5) * SPACEING_Y + PADDING_Y, 
                                    (q % 5) * SPACEING_X + PADDING_X, 
                                    math.floor(q / 5) * SPACEING_Y + PADDING_Y, width = LINEWIDTH, tags=mytag)

test_cells = [(1,1,0),
            (1,2,1),
            (1,3,0),
            (2,1,0),
            (2,2,1),
            (2,3,0),
            (3,1,0),
            (3,2,0),
            (3,3,0),
            (4,1,0),
            (4,2,1),
            (4,3,0)]

display_grid(create_adj_matrix(4,3, test_cells), 4, 3, (2,1), (2,4))

# This is how we change line color
# Here the line between vertex 1 and 2 is changed to red
# So, we maintain a list of the path A* takes
# then change the edges to show the final path
my_canvas.itemconfigure('(1,2)', fill='red')

root.mainloop()