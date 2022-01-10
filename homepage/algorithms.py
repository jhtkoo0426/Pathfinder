"""
This file contains classes for each path-finding algorithm.
"""
from heapq import heappush, heappop


# https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python
class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices  # ("A", "B", "C" ...)
        self.graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)  # get smallest distance
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + self.graph[min_vertex].get(neighbour, float("inf"))
                try:
                    if new_distance < unvisited[int(neighbour)]:
                        unvisited[int(neighbour)] = new_distance
                        parents[int(neighbour)] = min_vertex
                except KeyError:
                    pass
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break

        return parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[int(path[0])]
            path.insert(0, key)
            if key == start:
                break
        return path


