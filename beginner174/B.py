def main():
    n, d = map(int,input().split())
    import math
    count= 0
    pList = []
    for i in range(n):
        pList.append(list(map(int,input().split())))
    for p in pList:
        if math.sqrt(p[0]**2+p[1]**2) <= d:
            count += 1
    print(count)

if __name__ == "__main__":
    main()   
        