import math


def rotate(dx, dy, theta):
    theta = math.radians(theta)
    dx1 = dx * math.cos(theta) - dy * math.sin(theta)
    dy1 = dx * math.sin(theta) + dy * math.cos(theta)
    return dx1, dy1
