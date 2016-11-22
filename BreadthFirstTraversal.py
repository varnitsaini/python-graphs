"""
Illustrating breadth first traversal in Graph
The functioning is very similar to breadth first traversal in Trees
But the only difference is that we have to take care of the cycles
in the graph because we do not want to iterate over cyclic infinite loop

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

    """
    breadth first traversal for the graph
    """
    def breadthFirstTraversal(self, root):

        """
        initialise the list of nodes as False initially that is as we traverse the nodes
        in the graph we will keep marking the visited nodes as True
        """
        visitedNodes = [False] * (len(self.graph))

        queue = []

        """
        start with root node and append it in the queue
        and mark this visited node as True
        """
        queue.append(root)
        visitedNodes[root] = True

        """
        Traverse while queue is not empty, print the first element of the queue and pop it
        from the queue and push adjacent nodes of the current node to the list if they have
        not been visited before
        """
        while queue:

            root = queue.pop(0)
            print root,

            for vertices in self.graph[root]:
                if not visitedNodes[vertices]:
                    queue.append(vertices)
                    visitedNodes[vertices] = True

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

print graph.graph

graph.breadthFirstTraversal(2)