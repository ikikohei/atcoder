def main():
    import sys
    maxtime = 2*10**5 + 1
    N, W = map(int, input().split())
    timeScadule = [0]*maxtime
    for i in range(N):
        S, T, P = map(int, input().split())
        timeScadule[S] += P
        timeScadule[T] -= P
    if timeScadule[0] > W:
        print("No")
        sys.exit()
    for i in range(maxtime-1):
        timeScadule[i+1] += timeScadule[i]
        if timeScadule[i+1] > W:
            print("No")
            sys.exit()
    print("Yes")

if __name__=='__main__':
    main()