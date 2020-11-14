def linerityJudge(A,B,C):
    judge = False
    x_diff1 = B[0] - A[0]
    x_diff2 = C[0] - A[0]
    y_diff1 = B[1] - A[1]
    y_diff2 = C[1] - A[1]
    if y_diff1*x_diff2 == y_diff2*x_diff1:
        judge = True
    return judge

def main():
    N = int(input())
    positions = []
    judge = False
    for a in range(N):
        (x,y) = map(int,input().split())
        positions.append((x,y))
#    print(positions)    
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                # print("i:{}, j:{}, k:{}".format(i,j,k))
                if linerityJudge(positions[i],positions[j],positions[k]):
                    judge = True
                    exit
    print("Yes") if judge else print("No")

if __name__ == '__main__':
    main()

