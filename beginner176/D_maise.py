def useMasic(dq,p,maze,status):
    ph = p[0]
    pw = p[1]
    baseStatus = status[ph][pw]
    nh = min(ph-2,0)
    nw = min(pw-2,0)
    mh = min(ph+2,len(maze)-1)
    mw = min(pw+2,len(maze[0])-1)
    for h in range(nh,mh+1):
        for w in range(nw,mw+1):
            if maze[h][w] == "." and status[h][w] > baseStatus+1:
                status[h][w] = baseStatus + 1
                dq.append((h,w))

def checkadjcent(dq,p,maze,status):
    ph = p[0]
    pw = p[1]
    basestatus = status[ph][pw]
    if maze[ph + 1][pw] == "." and status[ph+1][pw] > basestatus:
        status[ph + 1][pw] = basestatus
        dq.appendleft((ph+1,pw))
    if maze[ph][pw + 1] == "." and status[ph][pw+1] > basestatus:
        status[ph][pw + 1] = basestatus
        dq.appendleft((ph,pw+1))
    if maze[ph - 1][pw] == "." and status[ph-1][pw] > basestatus:
        status[ph - 1][pw] = basestatus
        dq.appendleft((ph-1,pw))
    if maze[ph][pw - 1] == "." and status[ph][pw-1] > basestatus:
        status[ph][pw - 1] = basestatus
        dq.appendleft((ph,pw-1))

def wizardMaze(Ch,Cw,Dh,Dw,maze,status):
    import collections
    dq = collections.deque()
    redeq = collections.deque()
    dq.append((Ch,Cw))
    status[Ch][Cw] = 0
    while True:
        while len(dq) > 0:
            p = dq.popleft()
            redeq.appendleft(p)
            if p[0] == Dh and p[1] ==Dw: return status[p[0]][p[1]]
            checkadjcent(dq,p,maze,status)
        while len(redeq) > 0:
            pp = redeq.popleft()
            useMasic(dq,pp,maze,status)
        print(status)
        if not dq: break
    return -1

def main():
    MAXNUM = 10 ** 6 + 1
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    maze = [[i for i in range(W+2)] for j in range(H+2)]
    status = [[MAXNUM for i in range(W+2)] for j in range(H+2)]
    for i in range(H+2):
        if i==0 or i==H+1:
            pos = "#" * (W+2)
        else:
            pos = input()
        for j in range(W+2):
            if j == 0 or j == W+1:
                maze[i][j] = "#"
            else:
                maze[i][j] = pos[j-1]
    print(wizardMaze(Ch,Cw,Dh,Dw,maze,status))

if __name__=='__main__':
    main()
