"""
Illustrating adjacency list in undirected graph

Two classes are used, one for adding new Verted and
one for Graph class.

Space Complexity : O(|V| + |E|)
Time Complexity : O(|V|)
Where |V| -> vertex
      |E| -> edge
"""


"""
Creating vertex for adjacency list
"""
class Vertex:
    """
    defining the constructor for vertex class, which will have
    parameters id and edges to which it is connected to
    """
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    """
    adding an edge to the vertex node to nbr having the weight
    equal to "weight"
    """
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    """
    print in readable format, wherever vertex object is returned from
    the function call
    """
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    """
    get all the nodes to which the vertex is connected to
    """
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    """
    get the weight/distance from vertex object and the nbr(neighbour)
    """
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:

    """
    initialise the constructor for Graph object having vertex list ie
    total number of vertices in the graph and also maintain a count of
    number of vertices in the graph
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    """
    add the vertex to the graph with the given key. this function increments
    the vertices counter and creates a new vertex object and assigns the
    created vertex object to vertex list of the graph object
    """
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    """
    gets the vertex of the vertex list with given node id as n
    """
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    """
    adds the edge with the given weight between two vertices
    """
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

graph = Graph()

for i in range(7):
    print graph.addVertex(i)


graph.addEdge(3, 5, 20)
graph.addEdge(3, 7, 20)
graph.addEdge(3, 10, 20)
graph.addEdge(3, 11, 20)
print graph.getVertex(3)

for item, vertex in graph.vertList.iteritems():
    for vertexConnectedTo, edgeWeight in vertex.connectedTo.iteritems():
        print vertexConnectedTo.getId(), edgeWeight
    # print str(item), value.connectedTo


for vertex in graph:
    print vertex
    for vertexConnectedTo in vertex.getConnections():
        print("( %s , %s )" % (vertex.getId(), vertexConnectedTo.getId()))
        print vertex.connectedTo[vertexConnectedTo]