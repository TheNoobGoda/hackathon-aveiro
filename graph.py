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

    def get_distance(self,node1,node2):
        return mpu.haversine_distance((self.nodes[node1].x,self.nodes[node1].y),(self.nodes[node2].x,self.nodes[node2].y))
    

graph = Graph()

for i in range(10):
    graph.add_node(Node(random.randint(0,10),random.randint(0,10)))

for i in range(20):
    node1 = random.randint(0,9)
    node2 = random.randint(0,9)
    graph.add_edge(Edge(node1,node2,graph.get_distance(node1,node2)))

print(len(graph.nodes))
print(len(graph.edges))