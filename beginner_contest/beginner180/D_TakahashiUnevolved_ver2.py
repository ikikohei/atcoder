# 改造版　
def judgeMultiplication(X,A,B):
    return X*(A-1) < B

def main():
    import sys
    X, Y, A, B = map(int,input().split())
    count = 0
    while judgeMultiplication(X,A,B):
        X = X*A
        if X >= Y:
            print(count)
            sys.exit()
        count +=1
    count += (Y - X)//B
    if (Y-X)%B ==0: count -=1
    print(count)

if __name__=='__main__':
    main()