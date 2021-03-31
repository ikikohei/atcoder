def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list_sort = sorted(a_list)
    ans = 0
    fix_num = 998244352
    print(a_list_sort)
    count = 0
    for i, a in enumerate(a_list_sort):
        print("{} {}".format(i,a))
        ans += a * a
        # ans = ans % fix_num
        loop = 0
        count += 1
        for j in range(i+1, n):
            ans += a * a_list_sort[j] * 2**loop
            # ans = ans % fix_num
            count += 2**loop
            loop += 1
    ans = ans % fix_num
    print(ans)
    print(count)

if __name__=="__main__":
    main()