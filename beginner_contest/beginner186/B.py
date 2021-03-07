def main():
    inf = 1001
    h, w = map(int,input().split())
    blocks = []
    for hi in range(h):
        blocks.append(list(map(int,input().split())))
    minimumNum = inf
    for block in blocks:
        minimumNum = min(min(block),minimumNum)
    # print(minimumNum)
    ans = 0
    for block in blocks:
        for b in block:
            # print(b)
            ans += b - minimumNum
    print(ans)

if __name__ == "__main__":
    main()
            