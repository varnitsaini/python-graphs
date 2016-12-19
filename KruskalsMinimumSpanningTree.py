


class Graph:

    def __init__(self):
        self.vertices = []
        self.graph = []

    def addEdge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices.append(u)
        if v not in self.vertices:
            self.vertices.append(v)

        self.graph.append([u, v, weight])

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, a, b):
        aRoot = self.find(parent, a)
        bRoot = self.find(parent, b)

        if rank[aRoot] > rank[bRoot]:
            parent[bRoot] = aRoot
        elif rank[aRoot] < rank[bRoot]:
            parent[aRoot] = bRoot
        else:
            parent[bRoot] = aRoot
            rank[aRoot] += 1


    def KruskalMinSpanTree(self):

        resultingTree = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        i = 0
        e = 0

        for node in range(len(self.vertices)):
            parent.append(node)
            rank.append(0)

        while e < len(self.vertices) - 1:
            u, v, weight = self.graph[i]

            uRoot = self.find(parent, u)
            vRoot = self.find(parent, v)
            i += 1

            if uRoot != vRoot:
                e += 1
                resultingTree.append([u, v, weight])
                self.union(parent, rank, uRoot, vRoot)



        print "Following are the edges in the constructed MST"
        for u, v, weight in resultingTree:
            print ("%d -- %d == %d" % (u, v, weight))


g = Graph()
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMinSpanTree()