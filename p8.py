#Write a program to determine a minimum spanning tree of a graph using the Prim’s
#algorithm
import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.vertices):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.vertices
        parent = [-1] * self.vertices
        key[0] = 0
        mst_set = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

# Example usage
if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    print("Minimum Spanning Tree using Prim's Algorithm:")
    graph.prim_mst()
