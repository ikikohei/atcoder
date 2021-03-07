import heapq

#Define infinity
INFTY = 2**31 -1

class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = {}
        self.dist = INFTY
        self.pred = None

    # Define operator
    def __eq__(self, v):
        return self.dist == v.dist
        
    def __ne__(self, v):
        return self.dist != v.dist
    
    def __lt__(self, v):
        return self.dist < v.dist
    
    def __le__(self, v):
        return self.dist <= v.dist
    
    def __gt__(self, v):
        return self.dist > v.dist
    
    def __ge__(self, v):
        return self.dist >= v.dist
    
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.dist) + ", " + str_pred
    
# Change to the shortest path
def relax(u, v):
    if v.dist > u.dist + u.adj[v.id]:
        v.dist = u.dist + u.adj[v.id]
        v.pred = u.id
        return True
    else:
        return False

# dijkstra method
def dijkstra(vertices, src):
    #Initialize
    src.dist = 0
    q = [] #heapq
    for u in vertices:
        heapq.heappush(q, u)
    
    #Start search
    while len(q) > 0:
        # print_heap(q) # Display the heap
        u = heapq.heappop(q)
        for i in u.adj.keys():
            if relax(u, vertices[i]):
                heapq.heapify(q)
            
# Display the path
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id, end = " ")
    elif v.pred == None:
        print("\n Path does not exist")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id, end = " ")

def connect(vertices, i, j, weight):
    vertices[i].adj[j] = weight

def print_heap(q):
    print("[", end = " ")
    for i in q:
        print(i.id, end = " ")
    print("]")

if __name__ == "__main__":
    N = 5

    vertices = []
    for i in range(0, N):
        vertices.append(MyVertex(i))
    
    connect(vertices, 0, 1, 15)
    connect(vertices, 0, 4, 7)
    connect(vertices, 1, 2, 1)
    connect(vertices, 1, 4, 3)
    connect(vertices, 2, 3, 5)
    connect(vertices, 3, 2, 6)
    connect(vertices, 3, 0, 9)
    connect(vertices, 4, 1, 4)
    connect(vertices, 4, 2, 11)
    connect(vertices, 4, 3, 2)

    dijkstra(vertices, vertices[0])

    print("Path from vertex 0 to vertex 2: ", end = "")
    print_path(vertices, vertices[0], vertices[2])
    print("")

    for i in range(0, N):
        print(vertices[i].to_string())