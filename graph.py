import mpu
import random


random.seed(42)

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Edge:
    def __init__(self,node1,node2,distance,bidirectional = True):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance
        self.bidirectional = bidirectional

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self,node):
        self.nodes.append(node)

    def add_edge(self,edge):
        self.edges.append(edge)

    def get_edge_lenght(self,node1,node2):
        return mpu.haversine_distance((self.nodes[node1].x,self.nodes[node1].y),(self.nodes[node2].x,self.nodes[node2].y))
    
    def get_path(self,node1,node2):
        path = [node1]
        distance = 0

        while(True):
            distance2 = float('inf')
            node = path[len(path)-1]
            next_node = 0
            for edge in self.edges:
                    if edge.node1 == node and edge.node2 not in path:
                        new_distance = distance + edge.distance + self.get_edge_lenght(edge.node2, node2)
                        if new_distance < distance2:
                            distance2 = distance + new_distance
                            next_node = edge.node2

                    elif edge.node2 == node and edge.bidirectional and edge.node1 not in path:
                        new_distance = distance + edge.distance + self.get_edge_lenght(edge.node1, node2)
                        if new_distance < distance2:
                            distance2 = distance + new_distance
                            next_node = edge.node1
            path.append(next_node)
            if next_node == node2: break
            
        return path