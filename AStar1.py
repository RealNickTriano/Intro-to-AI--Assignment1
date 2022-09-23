import math 
class Vertex():
    def __init__(self, parent=None, location=None, legal=None):
        self.parent = parent
        self.location = location
        legal=0
        self.f = 0
        self.g = 0
        self.h = 0
def Solve(startingPoint,endPoint,dimensions):
    start = Vertex(None, startingPoint)
    start.f =0
    start.g=0
    start.h=0
    end=Vertex(None, endPoint)
    end.f=0
    end.g=0
    end.h=0
    fringeList=[]
    closedList=[]
    ##TODO need to make a relation from numeric representation of nodes to x,y coordinates 
   # digUr = position / dimensions
    #digUL = position / dimensions
   # digDR = position / dimensions
    #digDL = position / dimensions
    fringeList.append(start)
    i = 0
    fringeSize = len(fringeList)
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

        if position == endPoint:
            path =[]
            current = position
            while current is not None:
                path.append(current.location)
                current = current.parent
            return path[::-1]
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
