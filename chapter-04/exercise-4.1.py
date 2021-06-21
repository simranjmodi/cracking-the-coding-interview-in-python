"""
4.1 Route Between Nodes

Given a directed graph, design an algorithm to find out whether
there is a route between two nodes.
"""

from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_reachable(self, s, d):
        visited = [False] * (self.V)

        queue = deque()

        queue.append(s)
        visited[s] = True

        while queue:
            n = queue.popleft()

            if n == d:
                return True

            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False


