from asyncio.windows_events import NULL
import math
import heapq

def getVertexid(coords, m):
    id = coords[1] * (m + 1) + coords[0]
    return id

# Converts id to coordinates
def getVertexCoords(vid, m):
    coords = (vid % (m + 1), math.floor(vid / (m + 1)))
    return coords


def getDist(s,s2):
    a=getVertexCoords(s,4)
    b=getVertexCoords(s2,4)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    xVal=x2-x1
    yVal=y2-y1
    d=math.sqrt(pow(xVal,2)+pow(yVal,2))
    return d

def calculate_g(node, start):
    a=getVertexCoords(node,4)
    b=getVertexCoords(start,4)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    g = 0
    g=math.sqrt(2)*min(abs(x2-x1),abs(y2-y1))+max(abs(x2-x1),abs(y2-y1))-min(abs(x2-x1),abs(y2-y1))
    return g 
    

def calculate_h(node, end):
    a=getVertexCoords(node,4)
    b=getVertexCoords(end,4)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    h = 0
    h=math.sqrt(2)*min(abs(x2-x1),abs(y2-y1))+max(abs(x2-x1),abs(y2-y1))-min(abs(x2-x1),abs(y2-y1))
    return h 

def getPath(node):
    path =[node]
    current = node
    while current.parent is not current:
        path.append(current.parent)
        current = current.parent
    return path[::-1]

def getSuccessors(node):
    succ = []
    for item in matrix[node.name]:
        succ.append(item)
    return succ

def Solve(start, end):
    start.g_value = 0
    start.parent = start
    fringeList=[]
    heapq.heapify(fringeList)
    start.h_value = calculate_h(start, end)
    heapq.heappush(fringeList, (start, -1 * start.g_value + start.h_value))
    closedList=[]
    heapq.heapify(closedList)
    while len(fringeList) != 0:
        s = heapq.heappop(fringeList)
        if s.goal:
            return True, getPath(s)
        heapq.heappush(closedList, s)
        for s_prime in getSuccessors(s):
            if s_prime not in closedList:
                if s_prime not in fringeList:
                    s_prime.g_value = math.inf
                    s_prime.parent = NULL
                UpdateVertex(s, s_prime, fringeList)
    
    return False, []
    
    """
    pop first fringe item
    if its goal return path found

    otherwise
    closed.append current
    for s' in getSuccessors(s):
        if s' not in closed then
            if s' not in fringe then:
                g(s') = infinity
                parent(s') = null
            updateVertex(s,s')
    """
    for i in range(fringeSize):
        children =[]
        position = fringeList[0]
        placeHolder1 = 0
        for index, item in enumerate(fringeList):
            if item.f < position.f:
                position = item
                placeHolder1 = index
        fringeList.pop(placeHolder1)
        closedList.append(position)

        for nextVertex in[up, down, left, right, digUR, digUL, digDR, digDL]:
            node_position = (position.location[0] + nextVertex[0], position.position[1] + nextVertex[1])
            # TODO make user this works with the way were reciving input
            if nextVertex.legal == 0: 
                continue
            destination = Vertex(position, node_position)
            children.append(destination)
        for child in children:
            for childClosed in closedList:
                if child == childClosed:
                    continue
        if child.location == digUr or digUL or digDR or digDL:
            child.g = math.sqrt(2)
        else:
            child.g = position.g +1
        child.h = ((child.location[0] - end.location[0]) + (child.location[1] - end.location[1]))
        child.f = child.g + child.h
        for fringeVertex in fringeList:
                if child == fringeVertex and child.g > fringeVertex.g:
                    continue
        fringeList.append(child)

def UpdateVertex(s,s2, fringeList):
    if calculate_g(s) + getDist(s,s2) < calculate_g(s2):
        s2.parent = s
        if s2 in fringeList:
            fringeList.remove(s2)
            heapq.heapify(fringeList)
        heapq.heappush(fringeList, (s2, -1 * calculate_g(s2) + calculate_h(s2)))
    
