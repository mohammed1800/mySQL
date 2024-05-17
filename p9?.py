#Write a program to implement Dijkstra's algorithm to find the shortest paths from a given
#source node to all other nodes in a graph.
import heapq
import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def dijkstra(self, src):
        distance = [sys.maxsize] * self.vertices
        distance[src] = 0
        min_heap = [(0, src)]  # (distance, vertex)

        while min_heap:
            dist, u = heapq.heappop(min_heap)

            if dist > distance[u]:
                continue

            for v, weight in self.graph[u]:
                alt = dist + weight
                if alt < distance[v]:
                    distance[v] = alt
                    heapq.heappush(min_heap, (alt, v))

        self.print_shortest_paths(distance)

    def print_shortest_paths(self, distance):
        print("Vertex \tDistance from Source")
        for i in range(self.vertices):
            print(i, "\t", distance[i])

# Example usage
if __name__ == "__main__":
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    print("Shortest Paths from Source (Vertex 0) using Dijkstra's Algorithm:")
    graph.dijkstra(0)
