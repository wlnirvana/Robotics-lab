import math

def frontalDistance(A, B, R):

    top = (B[1]-A[1])*(A[0]-R[0]) - (B[0]-A[0])*(A[1]-R[1])
    bottom = (B[1]-A[1])*math.cos(R[2]) - (B[0]-A[0])*math.sin(R[2])

    return top/bottom

def intersection(R, m):
    x = R[0] + m * math.cos(R[2])
    y = R[1] + m * math.sin(R[2])

    return x, y

def valBetween(a, b, x):
    if a <= x <= b:
            return True
    elif a >= x >= b:
            return True

    return False

def isOnWall(A, B, intsect):
    return valBetween(A[0], B[0], intsect[0]) and \
            valBetween (A[1], B[1], intsect[1])

def wallInFront(A, B, intsect, m):
    return isOnWall(A, B, intsect) and m >= 0

def likelihood(z, m):
    p = (-(z-m)**2)/(2*0.527**2)
    return math.pow(math.e, p)
