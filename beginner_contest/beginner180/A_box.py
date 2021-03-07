def countBallInBox(N,A,B):
    return N-A+B

def main():
    N, A, B = map(int, input().split())
    print(countBallInBox(N,A,B))

if __name__ == '__main__':
    main()