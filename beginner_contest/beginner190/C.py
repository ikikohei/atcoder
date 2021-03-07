def main():
    n, m = map(int, input().split())
    condition = []
    for i in range(m):
        condition.append(list(map(int,input().split())))
    k = int(input())
    hito = []
    for j in range(k):
        hito.append(list(map(int, input().split())))
    hitoset = set()
    num = 0
    ans = 0
    maxans = 0
    for ki in range(2**k):
        num = 0
        ans = 0
        hitoset.clear()
        for l in format(ki, '0'+str(k)+'b'):
            hitoset.add(hito[num][int(l)])
            num += 1
        for mi in range(m):
            if condition[mi][1] in hitoset and condition[mi][0] in hitoset:
                ans += 1
        maxans = max(maxans, ans)
    print(maxans)

if __name__ == "__main__":
    main()