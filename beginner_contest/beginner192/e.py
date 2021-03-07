import heapq
import math

#Define infinity
INFTY = 10**19 -1
def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

class MyHeap:
    def __init__(self, arr):
        self.arr = arr
        self.size = 0
        self.create_min_heap()
    
    def min_heapify(self, index):
        left = self.get_left(index)
        right = self.get_right(index)
        if left < self.size and self.arr[left] < self.arr[index]:
            smallest = left
        else:
            smallest = index
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != index:
            swap(self.arr, index, smallest)
            self.min_heapify(smallest)
    
    def create_min_heap(self):
        self.size = len(self.arr)
        for i in range(math.floor(self.size / 2) -1, -1, -1):
            self.min_heapify(i)
        
    def get_parent(self, index):
        return math.floor((index + 1) / 2) - 1
    
    def get_left(self, index):
        return 2 * (index + 1) - 1
    
    def get_right(self, index):
        return 2 * (index + 1)

    def extract_min(self):
        if self.size < 1:
            print("heap is empty")
            return None
        
        min = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.arr.pop(self.size - 1)
        self.size -= 1
        self.min_heapify(0)

        return min

    def insert(self, val):
        self.size += 1
        self.arr.append(INFTY)
        self.decrease_val(self.size-1, val)
    
    def decrease_val(self, index, val):
        # if self.arr[index] < val:
        #     print("val is not decreased")
        #     return None
        
        self.arr[index] = val
        while index > 0 and self.arr[self.get_parent(index)] > self.arr[index]:
            swap(self.arr, index, self.get_parent(index))
            index = self.get_parent(index)
        
    def heap_sort(self):
        for i in range(self.size - 1, 0, -1):
            swap(self.arr, 0, i)
            self.size -= 1
            self.min_heapify(0)
        
        self.size = len(self.arr)
    
    def to_string(self):
        return str(self.arr[:self.size])


class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = {}
        self.dist = INFTY
        self.pred = None
        self.time = {} 

    # Define operator
    def __eq__(self, v):
        return self.id == v.id
        
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
    path_time = INFTY
    for i in range(len(u.time[v.id])):
        norikae = u.time[v.id][i] - u.dist % u.time[v.id][i]
        if u.dist % u.time[v.id][i] == 0: norikae = 0
        path_time = min(path_time, u.dist + u.adj[v.id][i] + norikae)
    if v.dist > path_time:
        v.dist = path_time 
        v.pred = u.id
        return True
    else:
        return False

# dijkstra method
def dijkstra(vertices, src):
    #Initialize
    src.dist = 0
    q = MyHeap([])
    for vertice in vertices:
        q.insert(vertice)
    #Start search
    while q.size > 0:
        # q.to_string()
        u = q.extract_min()
        # print(u.adj)
        for i in u.adj.keys():
            if relax(u, vertices[i]):
                # print(q.arr.index(vertices[i]))
                q.decrease_val(q.arr.index(vertices[i]), vertices[i])
            
# Display the path
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id, end = " ")
    elif v.pred == None:
        print("\n Path does not exist")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id, end = " ")
        print("dist{}".format(v.dist))

def connect(vertices, i, j, weight, time):
    if j not in vertices[i].adj:
        vertices[i].adj[j] = []
        vertices[j].adj[i] = []
        vertices[i].time[j] = []
        vertices[j].time[i] = []
    vertices[i].adj[j].append(weight)
    vertices[j].adj[i].append(weight)
    vertices[i].time[j].append(time)
    vertices[j].time[i].append(time)
    # print(vertices[i].time)
    # print(vertices[i].adj)

def print_heap(q):
    print("[", end = " ")
    for i in q:
        print(i.id, end = " ")
    print("]")

if __name__ == "__main__":
    n, m, x, y = map(int, input().split())
    vertices = []
    for i in range(0, n):
        vertices.append(MyVertex(i))
    for _ in range(0, m):
        a, b, t, k = map(int, input().split())
        connect(vertices, a-1, b-1, t, k)
    
    dijkstra(vertices, vertices[x-1])
    # for i in range(n):
        # print(vertices[i].dist)
    print_path(vertices, vertices[x-1], vertices[y-1])
    if vertices[y-1].dist >= INFTY:print(-1)
    else:
        print(vertices[y-1].dist)