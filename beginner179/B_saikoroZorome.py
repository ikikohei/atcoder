def main():
    import sys
    N = int(input())
    count = 0
    judge = False
    for i in range(N):
        D1, D2 = map(int,input().split())
        if D1 == D2:
            count += 1    
        else:
            count = 0
        if count == 3:
            judge = True
    print("Yes") if judge else print("No")

if __name__=='__main__':
    main()

        
