from telnetlib import theNULL

from main import getDist


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

def IsBlocked(s,s2):
    if=s2:
        s1+=1


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
            if yVal=0 and IsBlocked(x1+(sx-1)/2,y1) and IsBlocked(x1+(sx-1)/2,y1-1):
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
            if s2.f_value != 0 and IsBlocked(x1+x1+(sx-1)/2, y1+(sy-1)/2):
                return False
            if xVal = 0 and IsBlocked(x1,y1+(sy-1)/2) and IsBlocked(x1-1,y1+(sy-1)/2):
                return False
 