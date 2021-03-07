def wizardMaze(H,W,Ch,Cw,Dh,Dw,maze,status):
    import collections
    dq = collections.deque()
    redeq = collections.deque()
    dq.append((Ch,Cw))
    status[Ch][Cw] = 0
    diffs = [(0,1),(0,-1),(1,0),(-1,0)]
    # dh = [1,-1,0,0]
    # dw = [0,0,1,-1]
    reds = [-2,-1,0,1,2]
    while True:
        while len(dq) > 0:
            p = dq.popleft()
            redeq.append(p)
            if p[0] == Dh and p[1] ==Dw: return status[p[0]][p[1]]
            ph = p[0]
            pw = p[1]
            basestatus = status[ph][pw]
            for diff in diffs:
                if maze[ph+diff[0]][pw+diff[1]]=="." and status[ph+diff[0]][pw+diff[1]] > basestatus:
                    status[ph+diff[0]][pw+diff[1]]=basestatus
                    dq.append((ph+diff[0],pw+diff[1]))
        while len(redeq) > 0:
            pp = redeq.popleft()
            ph = pp[0]
            pw = pp[1]
            basestatus = status[ph][pw]
            for redh in reds:
                for redw in reds:
                    if 0 <= ph+redh < H+1 and 0 <= pw+redw < W+1 and status[ph+redh][pw+redw] > basestatus + 1 and maze[ph+redh][pw+redw] == ".":
                        status[ph+redh][pw+redw]=basestatus+1
                        dq.append((ph+redh,pw+redw))
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
    print(wizardMaze(H,W,Ch,Cw,Dh,Dw,maze,status))

if __name__=='__main__':
    main()
