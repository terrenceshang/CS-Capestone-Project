from asyncio.windows_events import NULL
import sys

class Edge:
    def __init__(self, destVert, cost):
        self.destVert = destVert
        self.cost = cost

class Vertex:
    def __init__(self, name, prev, scratch):
        self.name = name
        self.adj = {}
        self.dist = sys.maxsize
        self.prev = prev
        self.scratch = scratch
        self.visited = False

    def reset(self):
        self.dist = sys.maxsize
        self.prev = NULL
        self.scratch = 0
        self.visited = False
        self.adj = {}

    def add_neighbour(self, name, cost):
        self.adj[name] = cost

    def get_connections(self):
        return self.adj.keys()

    def get_name(self):
        return self.name

    def get_cost(self, neighbour):
        return self.adj[neighbour]

    def set_dist(self, dist):
        self.dist = dist

    def get_dist(self):
        return self.dist

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def getString(self):
        line = self.name + ' adjacent: ' + str([x.get_name for x in self.adj])
        return line

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, name):
        self.num_vertices += 1
        newVert = Vertex(name)
        self.vert_dict[name] = newVert
        return newVert

    def get_vertex(self, name):
        if name in self.vert_dict:
            return self.vert_dict[name]
        else:
            return None

    def add_edge(self, start, dest, cost):
        if start not in self.vert_dict:
            self.add_vertex(start)

        if dest not in self.vert_dict:
            self.add_vertex(dest)

        self.vert_dict[start].add_neighbour(self.vert_dict[dest], cost)
        self.vert_dict[dest].add_neighbour(self.vert_dict[start], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.set_previous = current
    

    def printPath(self, destName):
        destVert = self.get_vertex(destName)
        if destVert == None:
            return 'Destination vertex not found'
        else:
            distance = destVert.get_dist()
            if distance == sys.maxsize:
                return destVert.get_name() + ' is unreachable'
            else:
                