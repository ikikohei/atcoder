def main():
    n = int(input())
    num_list = [i for i in range(n+1)]
    fx_list = [0 for j in range(n+1)]
    for ni in range(1,n+1):
        for n_ni in num_list[0::ni]:
            # print(n_ni)
            fx_list[n_ni] += 1
    # print(fx_list)
    ans = 0
    for ai in range(n+1):
        ans += (ai) * fx_list[ai]
    print(ans)

if __name__ == "__main__":
    main()
