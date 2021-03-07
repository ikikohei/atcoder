# Define the type of status
WHITE = 0
GRAY = 1
BLACK = 2

# Define infinity
INFTY = 2**31 - 1

class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = set()
        self.color = WHITE
        self.dist = INFTY
        self.pred = None
    
    # display the information of vertices
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.color) + ", " + str(self.dist) + ", " + str_pred

# BFS
def bfs(vertices, src):
    # Initialize start vertex
    src.color =GRAY
    src.dist = 0
    src.pred = None

    #Search
    q = [src]
    while len(q) > 0:
        # u: search object
        u = q.pop(0)
        for i in u.adj:
            # v: next object
            v = vertices[i]
            if v.color == WHITE:
                v.color = GRAY
                v.dist = u.dist + 1
                v.pred = u.id
                q.append(v)
        u.color = BLACK

# Display the search history
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id, end = " ")
    elif v.pred == None:
        print("\nPath dose not exists")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id, end = " ")

# Connect the vertices
def connect(vertices, i, j):
    vertices[i].adj.add(j)
    vertices[j].adj.add(i)

if __name__ == "__main__":
    N = 8

    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))
    
    # connect(vertices, 0, 1)
    connect(vertices, 0, 7)
    connect(vertices, 1, 6)
    connect(vertices, 1, 2)
    connect(vertices, 2, 3)
    connect(vertices, 2, 5)
    connect(vertices, 3, 4)
    connect(vertices, 3, 5)
    connect(vertices, 4, 5)
    connect(vertices, 5, 6)

    bfs(vertices, vertices[0])

    print("Path from vertex 0 to vertex 7: ", end = " ")
    print_path(vertices, vertices[0], vertices[7])
    print("")

    for i in range(0, N):
        print(vertices[i].to_string())