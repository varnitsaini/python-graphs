"""
Illustrating bellman ford algorithm

Time Complexity : O(V*E)
where V -> number of vertices
      E -> number of edges
"""

class Graph():

    def __init__(self, vertices):
        self.verticesCount = vertices
        self.graph = []

    def addEdge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def bellmanFord(self, source):

        distance = [float('inf')] * self.verticesCount
        distance[source] = 0

        for vertice in range(self.verticesCount - 1):
            for u, v, weight in self.graph:
                if (distance[u] != float('inf')) and (distance[u] + weight < distance[v]):
                    distance[v] = distance[u] + weight

        for u, v, weight in self.graph:
            if (distance[u] != float('inf')) and (distance[u] + weight < distance[v]):
                print "Graph contains negative weight cycle."
                return

        for vertex in range(self.verticesCount-1):
            print("( vertext %s , distance %s )" % (vertex, distance[vertex]))


graph = Graph(6)
graph.addEdge(0, 1, -1)
graph.addEdge(0, 2, 4)
graph.addEdge(1, 2, 3)
graph.addEdge(1, 3, 2)
graph.addEdge(1, 4, 2)
graph.addEdge(3, 2, 5)
graph.addEdge(3, 1, 1)
graph.addEdge(4, 3, -3)

graph.bellmanFord(0)
