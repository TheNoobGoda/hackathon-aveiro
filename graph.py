import mpu
import heapq

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Edge:
    def __init__(self,node1,node2,distance,bidirectional = True):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance
        self.traffic_weight = 0 
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
        neighbors = []
        for edge in self.edges:
            if edge.node1 == node:
                neighbors.append((edge.node2, edge.distance))
            elif edge.bidirectional and edge.node2 == node:
                neighbors.append((edge.node1, edge.distance))
        return neighbors

    def dijkstra(self, start, end):
        """Implement Dijkstra's algorithm to find the shortest path from start to end."""
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
            
            for neighbor, edge_distance in self.get_neighbors(current_node):
                distance = current_distance + edge_distance
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
    
    def update_edge_weights(self, path):
        """Increase the traffic weight for each edge along the given path."""
        for i in range(len(path) - 1):
            node1, node2 = path[i], path[i+1]
            for edge in self.edges:
                if (edge.node1 == node1 and edge.node2 == node2) or (edge.node1 == node2 and edge.node2 == node1):
                    edge.traffic_weight += 1  # Increase weight due to traffic
                    break

    def find_closest_node(self, x, y):
        """Find the closest node to a given GPS location."""
        min_distance = float('inf')
        closest_node = None
        for i, node in enumerate(self.nodes):
            distance = mpu.haversine_distance((node.x, node.y), (x, y))
            if distance < min_distance:
                min_distance = distance
                closest_node = i
        return closest_node