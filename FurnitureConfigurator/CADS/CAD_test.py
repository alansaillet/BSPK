import cadquery as cq
from math import cos, sin, pi



def CAD1(l1,l2,l3):
    def surface(t1, t2):
        R = 10
        x = l1 * cos(t1 * 2 * pi) * cos(t2 * 2 * pi)
        y = l2 * sin(t1 * 2 * pi) * cos(t2 * 2 * pi)
        z = l3 * sin(t2 * 2 * pi)
        return (x, y, z)

    res = cq.Workplane().parametricSurface(surface, N=3,minDeg = 1, maxDeg = 1,tol=0.1)

    return res