import math
from Vertex import Vertex
from tkinter import *

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
    print(v)
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

def find_middle_edges(vertex_num):
    edges = []

    top_left = vertex_num - 6
    top = top_left + 1
    top_right = top + 1
    left = vertex_num - 1
    right = vertex_num + 1
    bot_left = left * 2
    bot = bot_left + 1
    bot_right = bot + 1

    edges.append(top_left)
    edges.append(top)
    edges.append(top_right)
    edges.append(left)
    edges.append(right)
    edges.append(bot_left)
    edges.append(bot)
    edges.append(bot_right)

    return edges

def create_adj_matrix(m, n):
    matrix = []
    
    for i in range(0, (m + 1) * (n + 1)):
        row = []
        for j in range(0, (m + 1) * (n + 1)):
            if (i == 6 and j in find_middle_edges(i)):
                row.append(1)
            else:
                row.append(0)
            
        matrix.append(row)

    return matrix



def create_circle(x, y, r, canvas): # center x,y, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    c = canvas.create_oval(x0, y0, x1, y1, fill='#000')
    canvas.tag_bind(c, "<Enter>", handle_enter_vertex)
    canvas.tag_bind(c, "<Leave>", handle_leave_vertex)
    # Hold vertex in array
    v = Vertex(c, x, y, False, False, 0, 0)
    vertices.append(v)

    return c

def display_grid(matrix, m, n): # n = dim of matrix n * n
    for i in range(0, (n + 1)):
        for j in range(0, (m + 1)):
            create_circle(j * 20 + 10, i * 20 + 10, 3,  my_canvas)
    for k in range(0, (m + 1) * (n + 1)):
        for q in range(0, (m + 1) * (n + 1)):
            if(matrix[k][q] == 1):
                # draw line from vertex i to vertex j
                my_canvas.create_line((k % 5) * 20 + 10, 
                                    math.floor(k / 5) * 20 + 10, 
                                    (q % 5) * 20 + 10, 
                                    math.floor(q / 5) * 20 + 10)

display_grid(create_adj_matrix(4,3), 4, 3)

root.mainloop()