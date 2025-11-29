"""
P: Find the distance between the closest pair of points in a plane.
Sol: Divide the plane into 2 halves and solve the problem for each half. For the points within the current minimum distance d to the separating line,
S_y (sorted by the y coordinate), check the distance to the 15 (could be reduced to 7) closest neighbors.
Complexity: O(n*log (n))
(Threshold: for a small number of points check all pairs of points - O(n**2))

Example:
4
0 1
1 1
1 0
0 0
d = 1.000000
"""

from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

def dist(p1, p2):
    """
    Computes the distance between 2 points.
    """
    return math.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))

def find_closest_distance(points_by_x, points_by_y):
    """
    Computes the minimum distance between 2 points in a plane.
    Parameters:
        points_by_x - points sorted by the x-coordinate
        points_by_y - points sorted by the y-coordinate
    Returns the minimum distance
    """
    n = len(points_by_x)
    if n < 4:
        # check all pairs of points
        min_dist = dist(points_by_x[-1], points_by_x[0])
        for i in range(n-1):
            min_dist = min(min_dist, dist(points_by_x[i], points_by_x[i+1]))
        return min_dist
    # divide the plane in 2 halves
    mid = int(len(points_by_x)/2)
    lx = points_by_x[:mid]
    rx = points_by_x[mid:]
    mid_x = rx[0].x
    ly = [p for p in points_by_y if p.x < mid_x]
    ry = [p for p in points_by_y if p.x >= mid_x]
    min_dist = min(find_closest_distance(lx, ly), find_closest_distance(rx, ry))
    # merge
    s_y = [p for p in points_by_y if abs(mid_x - p.x) < min_dist]
    for i, p in enumerate(s_y):
        for j in range(1, 16):
            # check 15 neighbors
            if i+j >= len(s_y):
                break
            min_dist = min(min_dist, dist(p, s_y[i+j]))
    return min_dist



if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split(" "))
        points.append(Point(x, y))

    points_by_x = sorted(points, key=lambda p: p.x)
    points_by_y = sorted(points, key=lambda p: p.y)

    if len(points) < 2:
        print("Too few points. Check input data")
    else:
        d = find_closest_distance(points_by_x, points_by_y)
        print("Minimum distance: %.6f" % d)
