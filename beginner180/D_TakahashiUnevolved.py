#　これは時間かかりすぎ。。。
def minPowerUp(X,A,B):
    return X*(A-1) if X*(A-1) < B else B

def main():
    X, Y, A, B = map(int,input().split())
    count = 0
    while True:
        X += minPowerUp(X,A,B)
        if X > Y: break
        print(X)
        count +=1
    print(count)

if __name__=='__main__':
    main()