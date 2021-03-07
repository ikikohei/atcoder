def g_1(n):
    import collections
    n_list = list(str(n))
    counter = collections.Counter(n_list)
    index = 0
    ans = 0
    for num in range(10):
        if str(num) not in counter:
            continue
        ans += int(str(num) * counter[str(num)]) * 10 ** index
        index += counter[str(num)]
    # print("g1 resurt{}".format(ans))
    return ans

def g_2(n):
    import collections
    n_list = list(str(n))
    counter = collections.Counter(n_list)
    index = 0
    ans = 0
    for num in reversed(range(10)):
        if str(num) not in counter:
            continue
        ans += int(str(num) * counter[str(num)]) * 10 ** index
        index += counter[str(num)]
    # print("g2 resurt{}".format(ans))
    return ans

def main():
    n, k = input().split()
    if k == '0': return print(n)
    ans = g_1(n) - g_2(n)
    for i in range(int(k)-1):
        if ans == g_1(ans) - g_2(ans): break
        ans = g_1(ans) - g_2(ans)
    print(ans)

if __name__ == "__main__":
    main()