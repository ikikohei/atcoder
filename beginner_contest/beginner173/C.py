def main():
    h, w, k = map(int, input().split())
    mass = []
    count = 0
    ans = 0
    for hi in range(h):
        mass.append(list(input()))
    loopnum = 2**(h+w)
    # print(loopnum)
    for num in range(loopnum):
        # print(num)
        # binnum = format(num,'012b')
        # print(binnum)
        for hi in range(h):
            for wi in range(w):
                if mass[hi][wi] == ".": continue
                if format(num>>hi, '012b')[-1]=="1" and format(num>>h+wi,'012b')[-1]=="1":
                    count += 1
        if count == k:
            # print(num)
            ans += 1
        count = 0
    print(ans)

if __name__ == "__main__":
    main()