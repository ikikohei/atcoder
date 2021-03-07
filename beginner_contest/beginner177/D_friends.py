#状態を定義。python の本参考
WHITE = 0
GRAY = 1
BLACK = 2

# 無限大の定義
INFTY = 2**31 -1

class MyVertex:
    def __init__(self,id):
        self.id = id
        self.adj = set()
        self.color = WHITE
        self.dist = INFTY
        self.pred = None

# 幅優先探索
def bfs(vertices, src):
    # 始点頂点の初期化
    src.color = GRAY
    src.dist = 0
    src.pred = None
    # 探索した数を記録
    count = 0
    #探索
    q = [src]
    while len(q)>0:
        u = q.pop(0)
        # pop したときにカウントを増やす
        count += 1
        for i in u.adj:
            v = vertices[i]
            if v.color == WHITE:
                v.color = GRAY
                v.dist = u.dist + 1
                v.pred = u.id
                q.append(v)
        u.color = BLACK
    # 探索結果を数で返す
    return count

def connect(vertices,i,j):
    vertices[i].adj.add(j)
    vertices[j].adj.add(i)

def main():
    N, M = map(int, input().split())
    vertices = []
    maxcount = 0
    for i in range(N):
        vertices.append(MyVertex(i))
    for j in range(M):
        A, B = map(int, input().split())
        connect(vertices,A-1,B-1)
    for k in range(N):
        if vertices[k].color==BLACK: continue
        count = bfs(vertices,vertices[k])
        maxcount = max(count,maxcount)
        if maxcount > N//2: break
    print(maxcount)

if __name__=='__main__':
    main()

