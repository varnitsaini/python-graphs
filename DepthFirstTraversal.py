"""
Illustrating depth first traversal in Graph
The functioning is very similar to depth first traversal in Trees
But the only difference is that we have to take care of the cycles
in the graph because we do not want to iterate over cyclic infinite loop
in case such exist in a graph

Time Complexity : O(V + E)
where V -> Number of vertex
      E -> number of edges
"""

"""
using defaultdict to create graph
"""
from collections import defaultdict

class Graph():

    """
    initialise the constructor for the graph to default dict having
    key as the vertex and list as the nodes to which vertex is connected to
    """
    def __init__(self):
        self.graph = defaultdict(list)

    """
    create the edges for the graph from u to v
    """
    def addEdge(self, u, v):
        self.graph[u].append(v)

    """depth first traversal"""
    def depthFirstTraversal(self, root):

        vistedNodes = [False] * (len(self.graph))

        self.depthFirstTraversalHelper(root, vistedNodes)

    def depthFirstTraversalHelper(self, root, visitedNodes):

        visitedNodes[root] = True
        print root,

        for vertex in self.graph[root]:
            if visitedNodes[vertex] == False:
                self.depthFirstTraversalHelper(vertex, visitedNodes)

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

print graph.graph

graph.depthFirstTraversal(2)