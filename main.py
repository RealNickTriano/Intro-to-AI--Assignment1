import math
from tkinter import *

root = Tk()
root.title('Codemy.com -  Canvas')
root.geometry("1920x1080")

my_canvas = Canvas(root, width=1920, height=1080, bg="white")
my_canvas.pack(pady=20)
vertices = []

lbl = Label(root)
lbl.place(x=200, y=20, anchor='nw')

def handle_enter_vertex(event):
    print('enter')
    # find the canvas item below mouse cursor
    item = my_canvas.find_withtag("current")
    # show it using the label
    lbl.config(text=item[0])
    # now we can get this vertex from our stored array of vertices
    # and check anything we want!

def handle_leave_vertex(event):
    print('leave')
    # clear the label text
    lbl.config(text="")

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
    vertices.append(c)

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

for i in range(0, 20):
    print(create_adj_matrix(4,3)[i])

print(my_canvas.coords(vertices[0]))

root.mainloop()