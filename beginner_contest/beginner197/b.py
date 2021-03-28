def main():
    h, w, x, y = map(int, input().split())
    s_list = []
    for i in range(h):
        s_list.append(input())
    diff = 0
    ans = 0
    while True:
        if x-1+diff < h and s_list[x-1+diff][y-1] != "#":
            ans += 1
            diff += 1
        else: break
    diff = 1
    while True:
        if x-1-diff >= 0 and s_list[x-1-diff][y-1] != "#":
            ans += 1
            diff += 1
        else: break
    diff = 1
    while True:
        if y-1+diff < w  and s_list[x-1][y-1+diff] != "#":
            ans += 1
            diff += 1
        else: break
    diff = 1
    while True:
        if y-1-diff >= 0 and s_list[x-1][y-1-diff] != "#":
            ans += 1
            diff += 1
        else: break
    print(ans)
 
if __name__=="__main__":
    main()