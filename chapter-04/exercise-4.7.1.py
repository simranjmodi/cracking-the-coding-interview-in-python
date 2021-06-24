"""
4.7 Build Order

You are given a list of projects and list of dependencies (which is a list of
pairs of projects, where the second project is dependent on the first project.
All of a project's dependencies must be built before the project is. Find a
build order that will allow the projects to be built. If there is no valid
build order, return an error.
"""

class Graph():
    def __init__(self,n):
        self.map = [[0 for i in range(n)] for i in range(n)]

    def add_edge(self,a,b):
        self.map[a][b] = 1

    def remove_edge(self,a,b):
        self.map[a][b] = 0

    def dependency(self,n):
        count = 0
        for i in range(len(self.map)):
            if self.map[i][n] == 1: count += 1
        return count

    def get_children(self,n):
        children = []
        row = self.map[n]
        for i in range(len(self.map)):
            if row[i] == 1: children.append(i)
        return children

def build_graph(projects, dependencies):
    n = len(projects)
    graph = Graph(n)

    for dependency in dependencies:
        start, end = dependency[0], dependency[1]
        graph.add_edge(start,end)
    return graph

def order_projects(graph,projects):
    n = len(projects)
    order = [0 for i in range(n)]

    offset = 0
    for project in projects:
        if graph.dependency(project) == 0:
            order[offset] = project
            offset += 1

    to_be_processed = 0
    while to_be_processed < n:
        current = order[to_be_processed]
        if current is None:
            return None
        children = graph.get_children(current)
        for child in children:
            graph.remove_edge(current,child)

        for child in children:
            if graph.dependency(child) == 0:
                order[offset] = child
                offset += 1

        to_be_processed += 1
    return order

def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph,projects)
