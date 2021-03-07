def main():
    import itertools
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list_sum = sum(a_list)
    ans = 0
    for i in range(n):
        ans += (n-1) * a_list[i] ** 2 
        a_list_sum = a_list_sum - a_list[i]
        ans -= 2 * a_list[i] * a_list_sum
    return print(ans)

if __name__=='__main__':
    main()

