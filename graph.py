import mpu
import heapq

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.num_cars = 0

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

    def get_edge_id(self,node1,node2):
        i = 0
        for edge in self.edges:
            if (edge.node1 == node1 and edge.node2 == node2) or (edge.node1 == node2 and edge.node2 == node1): return i
            else: i +=1

    def get_edge_lenght(self,node1,node2):
        return mpu.haversine_distance((self.nodes[node1].x,self.nodes[node1].y),(self.nodes[node2].x,self.nodes[node2].y))
    
    def get_neighbors(self, node):
        """
        Get neighboring nodes and the total weight (distance + traffic_weight) for each edge.
        """
        neighbors = []
        for edge in self.edges:
            if edge.node1 == node:
                total_weight = edge.distance
                neighbors.append((edge.node2, total_weight))
            elif edge.bidirectional and edge.node2 == node:
                total_weight = edge.distance
                neighbors.append((edge.node1, total_weight))
        return neighbors

    def dijkstra(self, start, end):
        """
        Implement Dijkstra's algorithm considering both distance and traffic weight.
        """
        distances = {node: float('inf') for node in range(len(self.nodes))}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, node)
        previous_nodes = {node: None for node in range(len(self.nodes))}
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node == end:
                break  # Found the shortest path to the target
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, edge_weight in self.get_neighbors(current_node):
                distance = current_distance + edge_weight + self.nodes[neighbor].num_cars
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Reconstruct the path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        
        path = path[::-1]  # Reverse the path to get it from start to end
        return path if path[0] == start else None  # Return path or None if no path is found


    def find_closest_nodes(self, x, y):
        """
        Find the closest and second closest nodes to a given GPS location.
        """
        distances = []
        for i, node in enumerate(self.nodes):
            distance = mpu.haversine_distance((node.x, node.y), (x, y))
            distances.append((distance, i))
        
        # Sort by distance
        distances.sort()

        closest_node = distances[0][1]  # Closest node
        return closest_node