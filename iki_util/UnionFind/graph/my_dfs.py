# Define the status
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
        self.dscv = INFTY
        self.cmpl = INFTY
        self.pred = None
    
    # Display the information of vertex
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.color) + ", " + str(self.dscv) + ", " + str(self.cmpl) + ", " + str_pred
    
# Sub function for dfs
def dfs(vertices, u, time):
    u.dscv = time
    time += 1
    u.color = GRAY
    for i in u.adj:
        v = vertices[i]
        if v.color == WHITE:
            v.pred = u.id
            dfs(vertices, v, time)
            time = v.cmpl + 1
    u.color = BLACK
    u.cmpl = time
    time += 1

#Display the path
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id, end = " ")
    elif v.pred == None:
        print("\n Path does not exist")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id, end = " ")

#Connect the vertices
def connect(vertices, i, j):
    vertices[i].adj.add(j)
    vertices[j].adj.add(i)

if __name__ == "__main__":
    N = 8
    vertices = []
    for i in range(N):
        vertices.append(MyVertex(i))

    # Set sample
    connect(vertices, 0, 1)
    connect(vertices, 0, 7)
    connect(vertices, 1, 6)
    connect(vertices, 1, 2)
    connect(vertices, 2, 3)
    connect(vertices, 2, 5)
    connect(vertices, 3, 4)
    connect(vertices, 3, 5)
    connect(vertices, 4, 5)
    connect(vertices, 5, 6)

    dfs(vertices, vertices[5], 0)

    print("Path from vertex 5 to vertex 7: ", end = " ")
    print_path(vertices, vertices[5], vertices[7])
    print("")

    for i in range(0, N):
        print(vertices[i].to_string())


