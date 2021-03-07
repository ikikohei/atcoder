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
    if j in vertices[i].adj:
        vertices[i].adj[j] = min(vertices[i].adj[j], weight)
    else: vertices[i].adj[j] = weight

def all_reset(vertices):
    for vertex in vertices:
        vertex.dist = INFTY
        vertex.pred = None

def print_heap(q):
    print("[", end = " ")
    for i in q:
        print(i.id, end = " ")
    print("]")

if __name__ == "__main__":
    n, m = map(int,input().split()) 

    vertices = []
    for i in range(0, n):
        vertices.append(MyVertex(i))
    
    for mi in range(0, m):
        a, b, weight = map(int, input().split())
        connect(vertices, a-1, b-1, weight)
    
    # dijkstra(vertices, vertices[0])

    for ni in range(0, n):
        ans = INFTY
        all_reset(vertices)
        dijkstra(vertices, vertices[ni])
        for i in range(0,n):
            if ni in vertices[i].adj:
                ans = min(vertices[i].dist + vertices[i].adj[ni], ans)
        # for adj in vertices[ni].adj:
        #     all_reset(vertices)
        #     dijkstra(vertices,vertices[adj])
        #     ans = min(vertices[ni].dist + vertices[ni].adj[adj], ans)
        if ans >= INFTY: ans = -1
        # for i in range(0, n):
        #     print(vertices[i].to_string())
        print(ans)
