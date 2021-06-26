def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        tmp = a_list[i] - 10
        tmp = max(tmp, 0)
        ans += tmp
    return print(ans)

if __name__=="__main__":
    main()

