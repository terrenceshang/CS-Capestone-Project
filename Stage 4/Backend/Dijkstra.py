#Author of Dijkstra algorithm: Alexey Klochay

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
        This method makes sure that the graph is symmetrical. In other words, if theres a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
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
    
def createGraph():
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
            
    graph = Graph(nodes, init_graph)
    
    return graph, lstACRoute, lstANRoute, lstASRoute, StationsArea

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

    return arrPath

def findRoute(start_node, end_node):
    graph, lstACRoute, lstANRoute, lstASRoute, StationsArea = createGraph()
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node = start_node)
    arrPath = print_result(previous_nodes, shortest_path, start_node=start_node, target_node= end_node)
    
    return arrPath

def getDuration(graph, start_node, end_node):
    return graph.value(start_node, end_node)

#not used as found a better approach in the searchRoute path
#checks the route given by dijkstra and ammends the path if it is not found
#returns 
def checkRoute(graph, route, path, conTrain):
    matches = []
    routeName = ""
    furthest = ""
    furPath = 0
    
    for lineRoute in route:
        routeName = lineRoute[0:1]
        duration = 0 
        prev = ""       
        pos = len(lineRoute)
        found = False
        furCount = 0
        for linePath in path:                                   
            bPathFound = False
            count = 0 
            furCount += 1                       
            for i in lineRoute:
                 
                count += 1
                if i == conTrain:
                    pos = count
                if found == True and len(prev) > 0:
                    duration += getDuration(graph, prev, linePath) 
                if i == linePath:
                    if len(conTrain) > 1 and linePath == path[0]:                        
                        if count > pos:
                            duration += getDuration(graph, conTrain, linePath)
                        else:
                            break
                    bPathFound = True 
                    found = True
                    if furPath < furCount:
                        furthest = linePath  
                          
                        furPath = furCount     
                    lineRoute = lineRoute[count:len(lineRoute)]
                    count = 0          
                    
                    prev = linePath
                    if linePath == path[path.__len__()-1]:
                        matches.append(routeName)
                        matches.append(duration)
                        matches.append(path[0])
                        matches.append(linePath)
                    break
            if bPathFound == False:
                break
            
    if matches.__len__() == 0:
        count = 0
        for i in range(len(path)):
            if path[i] == furthest:
                count = i
                break
        for repeat in range(2):
            if repeat == 0:
                matches.append(checkRoute(graph, route, path[0:count +1], conTrain))
            else:
                conTrain = ""
                matches.append(checkRoute(graph, route, path[count:len(path)], conTrain))
    return matches

#not used as found a better approach in the search route class to find the best route with shortest durations according to the dijkstra route
#gets the dijkstra route, seperates the route into the different areas and sends the different routes to checkroute
def getRoute(start_node, end_node):       
    found = False
    while found == False:
        graph, lstACRoute, lstANRoute, lstASRoute, StationsArea = createGraph()
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)
        arrPath = print_result(previous_nodes, shortest_path, start_node=start_node, target_node=end_node)
        
        area = []
        for i in arrPath:
            if len(StationsArea[i]) == 1 and StationsArea[i] not in area:                
                area.append(StationsArea[i])
        
        lines = []
        numArea = 0
        count = -1
        start = 0
        for line in arrPath:
            count += 1
            if area.__len__() > 1:
                if StationsArea[line] == area[numArea+1]:
                    lines.append(arrPath[start:count])
                    start = count
                    numArea += 1
            if numArea == (area.__len__()-1):
                lines.append(arrPath[start:len(arrPath)])
                break
  
        matches = []
        prev = ""
        for i in range(lines.__len__()):
            if area[i] == "C":
                passage = lstACRoute   
            elif area[i] == "N":
                passage = lstANRoute
            else:
                passage = lstASRoute
            matches = checkRoute(graph, passage, lines[i], prev)
            for line in lines[i]:
                if line == lines[i][len(lines[i])-1]:
                    prev = line
            
            return(matches)
              
        found = True
