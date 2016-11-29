"""
In this we illustrate cycle detection in undirected graph

Space Complexity : O(n)
Where n is number of vertices

Time Complexity : O(m)
Where m are number of operations

"""
from collections import defaultdict

class Graph:

    """
    Initialise number of vertices to zero and graph ds to defaultdict as list
    """
    def __init__(self):
        self.vertices = []
        self.graph = defaultdict(list)

    """
    Add edges to the graph and increment the counter for number
    of vertices
    """
    def addEdge(self, u, v):
        if u not in self.vertices:
            self.vertices.append(u)

        if v not in self.vertices:
            self.vertices.append(v)

        self.graph[u].append(v)


    """
    Finds the parent of the item
    """
    def findParent(self, parentList, item):
        if parentList[item] == -1:
            return item
        else:
            return self.findParent(parentList, parentList[item])

    """Sets the union of two disjoint sets"""
    def setUnion(self, parentList, a, b):
        aSet = self.findParent(parentList, a)
        bSet = self.findParent(parentList, b)

        parentList[aSet] = bSet

    """Checks whether a cycle exist in the graph or not"""
    def findCycle(self):

        parentList = [-1] * len(self.vertices)

        for node in self.graph:

            for item in self.graph[node]:
                itemParent = self.findParent(parentList, item)
                nodeParent = self.findParent(parentList, node)

                if itemParent == nodeParent:
                    return True
                self.setUnion(parentList, node, item)

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(3, 0)

if graph.findCycle():
    print "Graph contains cycle"
else:
    print "Graph do not contains cycle"
