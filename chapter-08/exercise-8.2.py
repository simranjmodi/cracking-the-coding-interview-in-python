"""
8.2 Robot Grid

Imagine a robot sitting on the upper left corner of grid with r rows
and c columns. The robot can only move in two directions, right and
down, but certain cells are "off limits" such that the robot cannot
step on them. Design and algorithm to find a path for the robot from
the top left to the bottom right.
"""

class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def get_path_aux(maze, row, col, path, failed_points):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    p = Point(row, col)

    if p in failed_points:
        return False

    is_at_origin = (row == 0) and (col == 0)

    if is_at_origin or \
        get_path_aux(maze, row, col - 1, path, failed_points) or \
        get_path_aux(maze, row -1, col, path, failed_points):
        path.append(p)
        return True

    failed_points[p.row] = p.col
    return False

def get_path(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    failed_points = {}
    if get_path_aux(maze, len(maze)-1, len(maze[0])-1, path, failed_points):
        return path
    return None