from array import array
from audioop import reverse
import sys
from turtle import st
import os
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    #print(unvisited_nodes)
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        #print(neighbors)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

    strPath = ",".join(reversed(path))
    arrPath = strPath.split(",")

    #print ("Hello " + arrPath) 
    return arrPath

def main():

    file = open(os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area North Duration.txt", "r")
    lstANDuration = []    
    for line in file:        
        lstANDuration.append ((line[:-1].split(",")))        
    file.close()
    
    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area Central Duration.txt", "r")
    lstACDuration = []
    for line in file:
        lstACDuration.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area South Duration.txt", "r")
    lstASDuration = []
    for line in file:
        lstASDuration.append ((line[:-1].split(",")))
    file.close()

    file = open(os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area North Train Route.txt", "r")
    lstANRoute = []    
    for line in file:        
        lstANRoute.append ((line[:-1].split(",")))        
    file.close()

    file = open(os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area Central Train Route.txt", "r")
    lstACRoute = []    
    for line in file:        
        lstACRoute.append ((line[:-1].split(",")))        
    file.close()

    file = open(os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area South Train Route.txt", "r")
    lstASRoute = []    
    for line in file:        
        lstASRoute.append ((line[:-1].split(",")))        
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Station.txt", "r")
    lstStation = []   
    StationsArea = {}
    for line in file:
        if len(line) > 1:
            arrline = []
            arrline.append((line[:-1].split(",")))
            StationsArea[arrline[0][0]] = arrline[0][1]
        pos = -1
        for i in line:
            pos += 1
            if i == ",":
                lstStation.append ((line[:pos]))
    file.close()
    
    nodes = lstStation
    #print(nodes)

    init_graph = {}
    for node in lstStation:
        init_graph[node] = {}

    for i in lstANDuration:        
        if len(i) > 1:
            init_graph[i[0]][i[1]] = int(i[2])

    for i in lstACDuration:        
        if len(i) > 1:
            #print(i)
            init_graph[i[0]][i[1]] = int(i[2])
    
    #print("")
    for i in lstASDuration:        
        if len(i) > 1:
            #print(i)
            init_graph[i[0]][i[1]] = int(i[2])

    
    found = False
    while found == False:
        graph = Graph(nodes, init_graph)
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Chris Hani")
        arrPath = print_result(previous_nodes, shortest_path, start_node="Chris Hani", target_node="Langa")
        
        bArea = False
        for i in arrPath:        
            if bArea == False:
                if len(StationsArea[i]) == 1:
                    area = StationsArea[i]
                    bArea = True
                
        route = []
        if area == "C":
            route = lstACRoute
        elif area == "N":
            route = lstANRoute
        else:
            route = lstASRoute
        
        for lineRoute in route:
            for linePath in arrPath:
                if StationsArea[linePath] == area:
                    bPathFound = False
                    count = 0
                    for i in lineRoute:
                        count += 1
                        if i == linePath:
                            bPathFound = True                             
                            lineRoute = lineRoute[count:len(lineRoute)]
                            count = 0
                            break
                else:
                    print("path found")
                    break
                if bPathFound == False:
                    break
        found = True

if __name__ == "__main__":
    main()