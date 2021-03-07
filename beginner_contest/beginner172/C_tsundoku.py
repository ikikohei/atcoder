def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_num = 0
    b_num = 0
    # total_time = 0
    read_time = 0
    ans = 0
    read_num = 0
    for i in range(n):
        if read_time + a_list[i] > k: break
        read_time += a_list[i]
        a_num += 1
    # print("A's read time: {} read num : {}".format(read_time, a_num))
    read_num = a_num
    while True:
        if b_num >= m or read_time + b_list[b_num] > k: break
        read_time += b_list[b_num]
        read_num += 1
        b_num += 1
    ans = read_num
    # print(ans)
    for j in reversed(range(a_num)):
        read_time -= a_list[j]
        read_num -= 1
        while True:
            if b_num >= m or read_time + b_list[b_num] > k: break
            read_time += b_list[b_num]
            read_num += 1
            b_num += 1
        ans = max(read_num, ans)
        # print(read_time)
        # print("b num :{}  j: {}".format(b_num,j))
    print(ans)

if __name__ == "__main__":
    main()
