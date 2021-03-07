def main():
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    c = [0]*n
    for ai in a:
        c[ai] += 1
    count = 0
    for ci in c:
        if ci < k:
            k = ci
        count += k
        if k == 0:
            break
    print(count)

if __name__ == "__main__":
    main()
       




