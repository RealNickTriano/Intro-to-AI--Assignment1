import math
from Vertex import Vertex
from tkinter import *
import heapq


PADDING_X = 10
PADDING_Y = 10
SPACEING_X = 20
SPACEING_Y = 20
NODE_RADIUS = 3
LINEWIDTH = 2
CAN_WIDTH = 0
CAN_HEIGHT = 0

FILE_PATH = 'demo.txt'

matrix_m = 0
matrix_n = 0
goal_position = (0, 0)
start_position = (0, 0)

root = Tk()
root.title('Codemy.com -  Canvas')
root.geometry("1920x1080")

my_canvas = Canvas(root, width=2050, height=1050, bg="white")
my_canvas.pack(pady=20)
vertices = []
matrix = []

# --------- Create labels ---------------

lbl_x_value = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='x: ')
lbl_y_value = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='y: ')
lbl_goal = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='goal: ')
lbl_start = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='start: ')
lbl_h_value = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='h: ')
lbl_g_value = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='g: ')
lbl_f_value = Label(my_canvas, bg='white', fg='black', font=('Arial', 16), text='f: ')
lbl_x_value.place(relx=0.1, rely=0.98, anchor='center')
lbl_y_value.place(relx=0.2, rely=0.98, anchor='center')
lbl_goal.place(relx=0.3, rely=0.98, anchor='center')
lbl_start.place(relx=0.4, rely=0.98, anchor='center')
lbl_h_value.place(relx=0.5, rely=0.98, anchor='center')
lbl_g_value.place(relx=0.6, rely=0.98, anchor='center')
lbl_f_value.place(relx=0.7, rely=0.98, anchor='center')

# --------- End Create labels ---------------

def updateLabels(v):
    lbl_x_value.config(text= 'x: ' + '{:.2f}'.format(v.x_pos))
    lbl_y_value.config(text= 'y: ' + '{:.2f}'.format(v.y_pos))
    lbl_goal.config(text= 'goal: ' + str(v.goal))
    lbl_start.config(text= 'start: ' + str(v.start))
    lbl_h_value.config(text= 'h: ' + '{:.2f}'.format(v.h_value))
    lbl_g_value.config(text= 'g: ' + '{:.2f}'.format(v.g_value))
    lbl_f_value.config(text= 'f: ' + '{:.2f}'.format(v.f_value))

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
    for i in range(0, (m + 1) * (n + 1)):
        row = []
        for j in range(0, (m + 1) * (n + 1)):
                row.append(0)
        matrix.append(row)
    
    # matrix is init with all 0's

    for item in cells:
        x = item[0] - 1 
        y = item[1] - 1
        blocked = item[2]
        # Find vertex id from (x, y)
        vid = y * (m + 1) + x
        if not blocked:
            matrix[vid][vid + 1] = 1
            matrix[vid + 1][vid] = 1
            matrix[vid][vid + m + 1] = 1
            matrix[vid + m + 1][vid] = 1
            matrix[vid][vid + m + 2] = 1
            matrix[vid + m + 2][vid] = 1
            matrix[vid + m + 1][vid + m + 2] = 1
            matrix[vid + m + 2][vid + m + 1] = 1
            matrix[vid + 1][vid + m + 1] = 1
            matrix[vid + m + 1][vid + 1] = 1
            matrix[vid + 1][vid + m + 2] = 1
            matrix[vid + m + 2][vid + 1] = 1
        else:
            pass

    return matrix

# Converts coordinates of node to node id
def getVertexid(coords, m):
    id = (coords[1] -  1) * (m + 1) + (coords[0] - 1)
    return id

# Converts id to coordinates
def getVertexCoords(vid, m):
    coords = (vid % (m + 1), math.floor(vid / (m + 1)))
    #print('COORDS FOR {}: {}'.format(vid, coords))
    return coords

# Arguments: x pos, y pos, r radius, goal bool, start bool
def create_circle(x, y, r, canvas, goal, start): # center x,y, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    if goal and start:
        c = canvas.create_oval(x0, y0, x1, y1, fill='purple', outline='purple')
    elif goal:
        c = canvas.create_oval(x0, y0, x1 , y1, fill='blue', outline='blue')
    elif start:
        c = canvas.create_oval(x0, y0, x1, y1, fill='red', outline='red')
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
                my_canvas.create_line((k % (m + 1)) * SPACEING_X + PADDING_X, 
                                    math.floor(k / (m + 1)) * SPACEING_Y + PADDING_Y, 
                                    (q % (m + 1)) * SPACEING_X + PADDING_X, 
                                    math.floor(q / (m + 1)) * SPACEING_Y + PADDING_Y, width = LINEWIDTH, tags=mytag, fill="black")
        

cells_input = []

with open(FILE_PATH, "r") as file_input:
    file_input = file_input.read().splitlines()


for i in file_input[3:]:
    cells_input.append(tuple(map(int, i.split(' '))))

# Dimensions of matrix 
matrix_m = int(file_input[2].split(' ')[0]) # 4 --> m rows
matrix_n = int(file_input[2].split(' ')[1]) # 3 --> n columns

goal_position = tuple(map(int, file_input[1].split(' '))) # (2, 1)
start_position = tuple(map(int, file_input[0].split(' '))) # (2, 4)

display_grid(create_adj_matrix(matrix_m, matrix_n, cells_input), matrix_m, matrix_n, goal_position, start_position)

#-----------------------------------------------------

def UpdateVertexTheta(s,s2, fringeList, start, end):
    if LineOfSight(s.parent, s2):
        #Path 2
        if s.parent.g_value + getDist(s.parent,s2) < s2.g_value:
            s2.g_value = s.parent.g_value + getDist(s.parent, s2)
            s2.parent = s.parent
            if s2 in fringeList:
                print('s` found in fringe list.\nRemoving from list and reheapifying...')
                fringeList.remove(s2)
                heapq.heapify(fringeList)
            s2.g_value = calculate_g(s2, start)
            s2.h_value = calculate_h(s2, end)
            s2.updateFValue()
        heapq.heappush(fringeList, (s2.g_value + s2.h_value, s2))
        print('Pushed s` to fringe: {}, {}'.format(s2.name - 1, s2.g_value + s2.h_value))

    else:
        #Path 1
        if s.g_value + getDist(s,s2) < s2.g_value:
            print('Found better path to s`, setting s` parent to s...')
            s2.parent = s
            if s2 in fringeList:
                print('s` found in fringe list.\nRemoving from list and reheapifying...')
                fringeList.remove(s2)
                heapq.heapify(fringeList)
            s2.g_value = calculate_g(s2, start)
            s2.h_value = calculate_h(s2, end)
            s2.updateFValue()
            heapq.heappush(fringeList, (s2.g_value + s2.h_value, s2))
            print('Pushed s` to fringe: {}, {}'.format(s2.name - 1, s2.g_value + s2.h_value))

def getDist(s,s2):
    a=getVertexCoords(s.name - 1, matrix_m)
    b=getVertexCoords(s2.name - 1, matrix_m)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    xDist=x2-x1
    yDist=y2-y1
    h=math.sqrt(math.pow(xDist, 2) +math.pow(yDist, 2))
    return h

#g is actual cost from start to node this uses h() calc which is an estimation
def calculate_g(node, start):
    g = getDist(node, node.parent) + node.parent.g_value
    return g
    
# Estimate of distance from node to goal (end)
def calculate_h(node,end):
    a=getVertexCoords(node.name - 1,matrix_m)
    b=getVertexCoords(end.name - 1,matrix_m)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    xDist=x2-x1
    yDist=y2-y1
    h=math.sqrt(math.pow(xDist, 2) +math.pow(yDist, 2))
    return h

def getPath(node):
    path =[node]
    current = node
    while current.parent is not current:
        path.append(current.parent)
        current = current.parent
    return path[::-1]

def getSuccessors(node, matrix):
    succ = []
    print('Getting Successors for node: {} '.format(node.name - 1))
    for index, item in enumerate(matrix[node.name - 1]):
        if item == 1:
            succ.append(vertices[index])
    #TODO: Strange interaction here
    """ print('succ')
    for s in succ:
        print(s.name - 1)"""
    return succ

def printList(list):
    for item in list:
        print(item)

def checkInList(item, fringeList):
    for x in fringeList:
        if item.name - 1 == x[1].name - 1:
            return False

    return True

def IsBlocked(xCoord,yCoord):
    x = int(xCoord)
    y = int(yCoord)
    x2= x - 1
    y2= y - 1
    blocked = matrix[getVertexid((x2, y2), matrix_m)][getVertexid((x, y), matrix_m)]
    print('{} is {}'.format((x, y), blocked))
    return not blocked

def LineOfSight(s,s2):
    a=getVertexCoords(s.name - 1, matrix_m)
    b=getVertexCoords(s2.name - 1, matrix_m)
    x0=a[0]
    y0=a[1]
    x1=b[0]
    y1=b[1]
    s2.f_value=0
    xVal=x1-x0
    yVal=y1-y0
    if yVal<0:
        yVal=yVal*-1
        sy=-1
    else:
        sy = 1
    if xVal < 0:
        xVal = xVal * -1
        sx =- 1
    else:
        sx = 1
    if xVal>yVal:
        while x0!=x1:
            print(x0,x1)
            s2.f_value = s2.f_value + yVal
            print(s2.f_value)
            if IsBlocked(x0 + ((sx-1) / 2), y0 + ((sy-1) / 2)):
                return False
            y0=y0+sy
            s2.f_value=s2.f_value-xVal
            if s2.f_value!=0 and IsBlocked(x0 + ((sx-1) / 2), y0 + ((sy-1) / 2)):
                return False
            if yVal==0 and IsBlocked(x0 + ((sx-1) / 2),y0) and IsBlocked(x0 + ((sx-1) / 2), y0 - 1):
                return False
            x0 = x0 + sx
    else:
        while y0 != y1:
            print(y0,y1)
            s2.f_value=s2.f_value+xVal
            if s2.f_value>yVal:
                print(s2.f_value)
                if IsBlocked(x0+(sx-1)/2,y0+(sy-1)/2):
                    return False
                x0=x0+sx
                s2.f_value=s2.f_value-yVal
            if s2.f_value != 0 and IsBlocked(x0+(sx-1)/2, y0+(sy-1)/2):
                return False
            if xVal == 0 and IsBlocked(x0,y0+(sy-1)/2) and IsBlocked(x0-1,y0+(sy-1)/2):
                return False
            y0=y0+sy
    return True

def thetaSolve(start,end,matrix):
    start.g_value=0
    start.parent=start
    fringeList=[]
    heapq.heapify(fringeList)
    start.h_value = calculate_h(start, end)
    start.updateFValue()
    heapq.heappush(fringeList, (start.g_value + start.h_value, start))
    start.h_value = getDist(start, end)
    closedList=[]
    heapq.heapify(closedList)
    while len(fringeList) != 0:
        s = heapq.heappop(fringeList)
        if s == end:
            return True, getPath(s[1])
        
        
        heapq.heappush(closedList, s[1])
        print('Pushed onto closed list: {}'.format(s[1].name - 1))
        print('Closed:')
        #print(closedList)
        for s_prime in getSuccessors(s[1], matrix):
            if s_prime not in closedList:
                 if checkInList(s_prime, fringeList) or len(fringeList) ==  0:
                    s_prime.g_value=math.inf
                    s_prime.parent=None
            UpdateVertexTheta(s[1],s_prime,fringeList,start,end)
    return False, []

#-------------------------------------------------------
# Call with start and goal
result, path = thetaSolve(vertices[getVertexid(start_position, matrix_m)], vertices[getVertexid(goal_position, matrix_m)], matrix)

if result:
    for i in range(0, len(path) - 1 ):
        tag = '({},{})'.format(path[i + 1].name - 1, path[i].name - 1)
        tag1 = '({},{})'.format(path[i].name - 1, path[i + 1].name - 1)
        my_canvas.itemconfigure(tag, fill='red')
        my_canvas.itemconfigure(tag1, fill='red')
else:
    lbl_path = Label(my_canvas, bg='white', fg='red', font=('Arial', 24), text='NO PATH')
    lbl_path.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()

#TODO getDist needs to change. can be calculate H




 
 