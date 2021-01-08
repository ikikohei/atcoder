def main():
    n = int(input())
    hito = []
    for i in range(n):
        hito.append(list(map(int,input().split())))
    hyo = []
    aoki = 0
    for i in range(n):
        aoki += hito[i][0]
        hyo.append(hito[i][0]*2+hito[i][1])
    hyo.sort(reverse=True)
    takahashi = 0
    count = 0
    for i in range(n):
        takahashi += hyo[i]
        count += 1
        if takahashi > aoki: return print(count)
    print(count)
        
if __name__ == "__main__":
    main()