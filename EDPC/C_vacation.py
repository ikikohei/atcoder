def vacation(al,bl,cl,N):
    hl = [[0 for i in range(3)] for j in range(10**5 + 1)]
    hl[0][0] = al[0]
    hl[0][1] = bl[0]
    hl[0][2] = cl[0]
    for i in range(N-1):
        hl[i+1][0] = max(hl[i][1]+al[i+1],hl[i][2]+al[i+1])
        hl[i+1][1]= max(hl[i][0]+bl[i+1],hl[i][2]+bl[i+1])
        hl[i+1][2] = max(hl[i][0]+cl[i+1],hl[i][1]+cl[i+1])
    return max(hl[N-1][0],hl[N-1][1],hl[N-1][2])

def main():
    N = int(input())
    al, bl, cl = [],[],[]
    for i in range(N):
        a,b,c = map(int, input().split())
        al.append(a)
        bl.append(b)
        cl.append(c)
    print(vacation(al,bl,cl,N))

if __name__=='__main__':
    main()
    
    

        