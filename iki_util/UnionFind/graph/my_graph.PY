# Vertex
class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = set()

    # display the information of the vertexes
    def to_string(self):
        return str(self.id) + ", adj = " + str(self.adj)
    
# connect two vertexes each way
def connect(vertices, i, j):
    vertices[i].adj.add(j)
    vertices[j].adj.add(i)

if __name__ == "__main__":
    N = 5

    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))

    # set the edges
    connect(vertices, 0, 1)
    connect(vertices, 0, 4)
    connect(vertices, 1, 2)
    connect(vertices, 1, 3)
    connect(vertices, 2, 4)
    connect(vertices, 2, 3)
    connect(vertices, 3, 2)
    connect(vertices, 4, 3)

    # display each vertices
    for i in range(0, N):
        print(vertices[i].to_string())