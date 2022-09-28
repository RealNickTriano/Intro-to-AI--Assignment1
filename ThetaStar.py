from json.encoder import INFINITY
from main import getDist

#TODO getDist needs to change. can be calculate H
def UpdateVertexTheta(s,s2, fringeList, start, end):
    if LineOfSight(s.parent, s2):
        if s.parent.g_value+getDist(s.parent,s2)<s2.g_value:
            s2.g_value=s.parent.g_value+getDist(s.parent, s2)
            s2.parent=s.parent
            if s2 in fringeList:
                print('s` found in fringe list.\nRemoving from list and reheapifying...')
                fringeList.remove(s2)
                heapq.heapify(fringeList)
        heapq.heappush(fringeList, (s2.g_value + s2.h_value, s2))
        print('Pushed s` to fringe: {}, {}'.format(s2.name - 1, s2.g_value + s2.h_value))

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
def getVertexid(coords, m):
    id = (coords[1] -  1) * (m + 1) + (coords[0] - 1)
    return id
def IsBlocked(xCoord,yCoord):
    x2=xCoord-1
    y2=yCoord-1
    x3=xCoord+1
    y3=yCoord+1
    tuple2=[x2,y2]
    tuple3=[x3,y3]
    ID1=getVertexid(tuple2,m)
    ID2=getVertexid(tuple3,m)
    ID3=matrix[ID1,ID2]
    if ID3 != 0:
        return True

def calculate_g(node, start):
    g = getDist(node, node.parent) + node.parent.g_value
    return g

def calculate_h(node,end):
    a=getVertexCoords(s.name - 1,matrix_m)
    b=getVertexCoords(s2.name - 1,matrix_m)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    xDist=x2-x1
    yDist=y2-y1
    h=math.sqrt(math.pow(xDist),2 +math.pow(yDist),2)

def LineOfSight(s,s2):
    a=getVertexCoords(s.name - 1,matrix_m)
    b=getVertexCoords(s2.name - 1,matrix_m)
    x1=a[0]
    y1=a[1]
    x2=b[0]
    y2=b[1]
    s2.f_value=0
    sx=1
    sy=1
    xVal=x2-x1
    yVal=y2-y1
    if yVal<0:
        yVal=yVal*-1
        sy=-1
    if xVal<0:
        xVal=xVal*-1
        sx=-1
    if xVal>yVal:
        while x1!=x2:
            s2.f_value=s2.f_value+yVal
            if IsBlocked(x1+(sx-1)/2, y1+(sy-1/2)):
                return False
            y1=y1+sy
            s2.f_value=s2.f_value-xVal
            if s2.f_value!=0 and IsBlocked(x1+(sx-1)/2,y1+(sy-1)/2):
                return False
            if yVal==0 and IsBlocked(x1+(sx-1)/2,y1) and IsBlocked(x1+(sx-1)/2,y1-1):
                return False
            x1=x1+sx

    else:
        while y1 != y2:
            s2.f_value=s2.f_value+xVal
            if s2.f_value>yVal:
                if IsBlocked(x1+(sx-1)/2,y1+(sy-1)/2):
                    return False
                x1=x1+sx
                s2.f_value=s2.f_value-yVal
            if s2.f_value != 0 and IsBlocked(x1+(sx-1)/2, y1+(sy-1)/2):
                return False
            if xVal == 0 and IsBlocked(x1,y1+(sy-1)/2) and IsBlocked(x1-1,y1+(sy-1)/2):
                return False
 
def thetaSolve(start,end,matrix):
    start.g_value=0
    start.parent=start
    fringeList=[]
    heapq.heapify(fringeList)
    
    start.h_value = getDist(start, end)
    while len(fringeList) != 0:
        s = heapq.heappop(fringeList)
        if s == end:
            return True, getPath(s[1])
        closedList=[]
        heapq.heapify(closedList)
        heapq.heappush(closedList, s[1])
        print('Pushed onto closed list: {}'.format(s[1].name - 1))
        print('Closed:')
        for s_prime in getSuccessors(s[1], matrix):
            if s_prime not in closedList:
                 if checkInList(s_prime, fringeList):
                    s_prime.g_value=INFINITY
                    s_prime.parent=None
            UpdateVertexTheta(s[1],s_prime,fringeList,start,end)
    return "No Path Found" 